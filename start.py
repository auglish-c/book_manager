from flask import Flask, jsonify, request
from app.account import users
from app.book import book

app = Flask(__name__)
db = users.connect_db()

@app.route('/')
def hello():
    return "hello world"

@app.route('/account/register', methods = ['POST'])
def register():
    res = users.register(db, request.form['mail_address'], request.form['password'])
    return res

@app.route('/account/login', methods = ['POST'])
def login():
    res = users.login(db, request.form['mail_address'], request.form['password'])
    return str(res)

@app.route('/book/regist', methods = ['POST'])
def regist():
    data = { 'user_id'      : request.form['user_id'],
             'image_data'    : request.form['image_data'],
             'name'         : request.form['name'],
             'price'        : request.form['price'],
             'purchase_date': request.form['purchase_date']}
    res = book.register(db, data)
    return str(res)

@app.route('/book/update', methods = ['POST'])
def update():
    data = { 'image_data': request.form['image_data'],
             'name': request.form['name'],
             'price': request.form['price'],
             'purchase_date': request.form['purchase_date']}
    res = book.update(db, request.form['id'], data)
    return str(res)

@app.route('/book/get', methods = ['POST'])
def get():
    res = book.get(db, request.form['page'], request.form['user_id'])
    return jsonify(result=res)

if __name__ == '__main__':
    app.run()
