from flask import Blueprint, render_template, request, redirect, session
import bikeseoul.models.board as bo

bp = Blueprint('board', __name__, url_prefix='/board')
board_service = bo.BoardService()
reply_service = bo.ReplyService()


@bp.route('/add')
def add_form():
    if 'id' not in session:
        return redirect('/member/login')
    else:
        return render_template('board/form.html')


@bp.route('/add', methods=['POST'])
def add():
    id = session['id']
    title = request.form['title']
    content = request.form['content']
    b = bo.Board(writer=id, title=title, content=content)
    board_service.addBoard(b)
    return redirect('/board')


@bp.route('/')
def list_page():
    board = board_service.getAll()
    return render_template('board/list.html', board=board)


@bp.route('/content')
def content():
    num = request.args.get('num', '', int)
    b = board_service.getByNum(num)
    r = reply_service.getBoardReply(num)
    return render_template('board/content.html', b=b, r=r)


@bp.route('/edit')
def edit_form():
    if 'id' not in session:
        return redirect('/member/login')
    else:
        num = request.args.get('num', '', int)
        b = board_service.getByNum(num)
        return render_template('board/edit.html', b=b)


@bp.route('/edit', methods=['POST'])
def edit_content():
    num = request.form['num']
    title = request.form['title']
    content = request.form['content']
    b = bo.Board(num=num, title=title, content=content)
    board_service.editContent(b)
    return redirect('/board')


@bp.route('/del')
def del_content():
    num = request.args.get('num', '', int)
    board_service.delByNum(num)
    return redirect('/board')


@bp.route('/reply', methods=['POST'])
def write_reply():
    reply_writer = session['id']
    board_num = request.form['board_num']
    content = request.form['content']
    reply = bo.Reply(reply_writer=reply_writer, board_num=board_num, content=content)
    reply_service.addReply(reply)
    return redirect('/board/content?num='+board_num)


@bp.route('/delreply')
def delete_reply():
    board_num = request.args.get('num', '', int)
    reply_num = request.args.get('reply_num', '', int)
    reply_service.delByNum(reply_num)
    return redirect('/board/content?num='+str(board_num))

