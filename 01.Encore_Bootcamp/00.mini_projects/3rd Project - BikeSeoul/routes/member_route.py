from flask import Blueprint, render_template, request, redirect, session, flash
import bikeseoul.models.member as mem

bp = Blueprint('member', __name__, url_prefix='/member')
mem_service = mem.MemberService()


@bp.route('/join')
def join_form():
    if 'id' in session:
        flash("이미 로그인되어 있습니다 :)")
        return redirect('/')
    else:
        return render_template('member/join.html')


@bp.route('/join', methods=['POST'])
def join():
    id = request.form['id']
    password = request.form['password']
    name = request.form['name']
    gender = request.form['gender']
    age = request.form['age']

    mem_check = mem_service.getMem(id)
    if mem_check is None:
        m = mem.Member(id, password, name, gender, age)
        mem_service.addMem(m)
        flash("축하합니다! 가입이 완료되었습니다. 로그인을 해주세요.")
        return render_template('member/login.html')
    else:
        flash("이미 존재하는 아이디입니다.")
        return render_template('member/join.html')


@bp.route('/temp')
def temp():
    return redirect('/')


@bp.route('/login')
def login_form():
    return render_template('member/login.html')


@bp.route('/login', methods=['POST'])
def login():
    path = 'member/login.html'
    id = request.form['id']
    password = request.form['password']
    m = mem_service.getMem(id)
    if m == None:
        flash("아이디가 존재하지 않습니다.")
    else:
        if password == m.password:
            session['id'] = id
            print(session['id'])
            path = 'index.html'
        else:
            flash("비밀번호를 틀리셨습니다.")
    return render_template(path)


@bp.route('/logout')
def logout():
    if 'id' in session:
        session.pop('id')
    return redirect('/')


@bp.route('/info')
def get_member():
    if 'id' in session:
        id = session['id']
        m = mem_service.getMem(id)
    else:
        return redirect('/member/login')
    return render_template('member/detail.html', mem=m)


@bp.route('/edit', methods=['POST'])
def edit_mem():
    id = request.form['id']
    password = request.form['password']
    name = request.form['name']
    gender = request.form['gender']
    age = request.form['age']
    m = mem.Member(id, password, name, gender, age)
    mem_service.editMem(m)
    flash("회원정보가 수정되었습니다")
    return redirect('/member/info')


@bp.route('/del')
def delete_mem():
    if 'id' in session:
        id = session['id']
    mem_service.delMem(id)
    session.pop('id')
    return redirect('/')