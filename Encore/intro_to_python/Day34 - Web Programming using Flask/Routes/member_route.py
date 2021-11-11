from flask import Blueprint, render_template, request, redirect, session
import Board.Models.member as mem

bp = Blueprint('member', __name__, url_prefix='/member')  #블루프린트 객체 생성
mem_service = mem.MemberService()

@bp.route('/join')
def join_form():
    return render_template('member/join.html')

@bp.route('/join', methods=['POST'])
def join():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    email = request.form['email']

    mem_check = mem_service.getMem(id)
    if mem_check == None:
        m = mem.Member(id, pwd, name, email)
        mem_service.addMem(m)
        return redirect('/')
    else:
        return '이미 존재하는 ID입니다.'

@bp.route('/login')
def login_form():
    return render_template('member/login.html')

@bp.route('/login', methods=['POST'])
def login():
    msg = ''
    path = 'member/login.html'
    id = request.form['id']
    pwd = request.form['pwd']
    m = mem_service.getMem(id)
    if m == None:
        msg = "존재하지 않는 아이디"
    else:
        if pwd == m.pwd:
            session['id'] = id
            print(session['id'])
            path = 'index.html'
            msg = "로그인 성공"
        else:
            msg = "패스워드 불일치"
    return render_template(path, msg=msg)

@bp.route('/logout')
def logout():
    if 'id' in session:
        session.pop('id', None)
    return redirect('/')

@bp.route('/getmember')
def get_member():
    if 'id' in session:
        id = session['id']
        m = mem_service.getMem(id)
    else:
        return '먼저 로그인을 해주세요'
    return render_template('member/detail.html', mem=m)

@bp.route('/edit', methods=['POST'])
def edit_mem():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    email = request.form['email']
    m = mem.Member(id, pwd, name, email)
    mem_service.editMem(m)
    return redirect('/')

@bp.route('/del')
def delete_mem():
    if 'id' in session:
        id = session['id']
    mem_service.delMem(id)
    session.pop('id', None)
    return redirect('/')