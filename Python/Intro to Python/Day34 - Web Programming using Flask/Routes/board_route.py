from flask import Blueprint, render_template, request, redirect, session
import Board.Models.board as bo

bp = Blueprint('board', __name__, url_prefix='/board')
board_service = bo.BoardService()

@bp.route('/add')
def add_form():
    return render_template('board/form.html')

@bp.route('/add', methods=['POST'])
def add():
    id = request.form['id']
    title = request.form['title']
    content = request.form['content']
    b = bo.Board(writer=id, title=title, content=content)
    board_service.addBoard(b)
    return redirect('/board/list')

@bp.route('/list')
def list():
    board = board_service.getAll()
    return render_template('board/list.html', board=board)

@bp.route('/content')
def content():
    num = request.args.get('num', '', int)
    b = board_service.getByNum(num)
    return render_template('board/detail.html', b=b)

@bp.route('/edit')
def edit_form():
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
    return redirect('/board/list')

@bp.route('/del')
def del_content():
    num = request.args.get('num', '', int)
    board_service.delByNum(num)
    return redirect('/board/list')