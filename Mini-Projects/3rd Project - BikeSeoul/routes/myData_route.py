from flask import Blueprint, render_template, request, redirect, session
import bikeseoul.models.myData as md
bp = Blueprint('mydata', __name__, url_prefix='/mydata')
mydataService = md.MyDataService()

@bp.route('/')
def list():
    datas = mydataService.getAll()
    return render_template('myData/list.html', datas=datas)

@bp.route('/add')
def add_form():
    return render_template('myData/form.html')

@bp.route('/add', methods=['POST'])
def add():
    upload_path = 'static/product/'
    f = request.files['img_path']
    fname = upload_path + f.filename
    f.save(fname)
    name = request.form['name']
    price = request.form.get('price', 0, int)
    amount = request.form.get('amount', 0, int)
    img_path = '/' + fname
    p = prod.Product(name=name, price=price, amount=amount, img_path=img_path)
    mydataService.addProduct(p)
    return redirect('/product/')

@bp.route('/get')
def get():
    num = request.args.get('num', 0, int)
    p = prodService.getProduct(num)
    return render_template('product/detail.html', p=p)