from flask import Flask, jsonify, request, session
from app.account import users
from app.book import book
from flask.ext.login import LoginManager, UserMixin, login_required,\
                           login_user, logout_user, make_secure_token

app = Flask(__name__)
db = users.connect_db()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@app.route('/')
def hello():
    return "hello world"

@app.route('/account/register', methods = ['POST'])
def register():
    print request.values
    res = users.register(db, request.form['mail_address'], request.form['password'])
    print res
    return str(res)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/account/login', methods = ['POST'])
def login():
    print request.values
    res = users.login(db, request.form['mail_address'], request.form['password'])
    if res:
        user = User(res['mail_address'], res['password'])
        session['username'] = res['id']
        print session
    return str(res)

@app.route('/book/regist', methods = ['POST'])
def regist():
    print request.values
    data = { 'user_id'      : request.form['user_id'],
             'image_data'    : request.form['image_data'],
             'name'         : request.form['name'],
             'price'        : request.form['price'],
             'purchase_date': request.form['purchase_date']}
    res = book.register(db, data)
    return str(res)

@app.route('/book/update', methods = ['POST'])
def update():
    print request.values
    data = { 'image_data': request.form['image_data'],
             'name': request.form['name'],
             'price': request.form['price'],
             'purchase_date': request.form['purchase_date']}
    res = book.update(db, request.form['id'], data)
    return str(res)

@app.route('/book/get', methods = ['GET'])
def get():
    print request.values
    res = book.get(db, request.args.get('page'), request.args.get('user_id'))
    return jsonify(result=res)

class User(UserMixin):
    def __init__(self, id, passwd):
        self.id = id
        self.name = "user" + str(id)
        self.password = passwd

@login_manager.user_loader
def user_loader(email):
   user = User()
   user.id = email
   print user.id
   return user

@login_manager.request_loader
def request_loader(request):
   user = User()
   user.id = request.form['mail_address']
   print user.id
   return user

if __name__ == '__main__':
    app.run(debug=True)
