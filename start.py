from flask import Flask, jsonify, request, session, abort, Response
from app.account import users
from app.book import book
from flask.ext.login import LoginManager, UserMixin, login_required,\
                           login_user, logout_user, make_secure_token
import base64

app = Flask(__name__)
db = users.connect_db()

app.config.update(
    DEBUG = True,
    SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@app.route('/')
def hello():
    return "hello world"

@app.route('/signup', methods = ['POST'])
def register():
    print request.json
    email = request.json['email']
    passwd = request.json['password']
    res = users.register(db, request.json['email'], request.json['password'])
    print "RES"
    print res
    if res > 0:
        user = User(email, passwd)
        login_user(user)
        user_token=make_secure_token(session['_id'])
        print session
        return jsonify(request_token=user_token,
                       user_id=res)
    return error_response(400)

@app.route('/login', methods = ['POST'])
def login():
    json = request.json
    print json
    res = users.login(db, json['email'], json['password'])
    print res
    
    if res == users.FAILED:
        response = jsonify(error_message="ERROR : no user")
        response.status_code = 400
        return response
    user = User(json['email'], json['password'])
    login_user(user)
    user_token =  make_secure_token(session['_id'])
    print "SESSION"
    print session
    return jsonify(request_token=user_token,
                   user_id=res)

@app.route("/logout")
@login_required
def logout():
    if check_auth(request) != True:
        return error_response(401)
    return jsonify(is_success=logout_user())

@app.route('/books', methods = ['POST'])
def regist():
    if check_auth(request) != True:
        return error_response(401)
    print request.json
    data = { 'user_id'      : request.json['user_id'],
             'image_data'    : request.json['image_data'],
             'name'         : request.json['name'],
             'price'        : request.json['price'],
             'purchase_date': request.json['purchase_date']}
    res = book.register(db, data)
    print "RES : "
    print  res
    return jsonify(book_id=res)

@app.route('/books/<id>', methods = ['PATCH'])
def update(id):
    if check_auth(request) != True:
        return error_response(401)
    print request.values
    data = { 'image_data': request.json['image_data'],
             'name': request.json['name'],
             'price': request.json['price'],
             'purchase_date': request.json['purchase_date']}
    res = book.update(db, id, data)
    return jsonify(book_id=res)

@app.route('/books', methods = ['GET'])
def get():
    if check_auth(request) != True:
        return error_response(401)
    print request.values
    res = book.get(db, request.args.get('page'), request.args.get('user_id'))
    return jsonify(result=res)

class User(UserMixin):
    def __init__(self, id, passwd):
        self.id = id
        self.name = "user" + str(id)
        self.password = passwd

@login_manager.user_loader
def user_loader(req):
    print "user"
    user = User(req, req)
    return user

@login_manager.request_loader
def request_loader(request):
    print "request"
    user = User(request.form['email'], request.form['password'])
    return user

def check_auth(request):
    print "REQUEST HEADER"
    print request.headers
    print "SESSION"
    print session
    if 'Authorization' not in request.headers:
        print 'nothing auth'
        return False
    if '_id' not in session:
        print 'without _id'
        return False

    header_token = request.headers['Authorization']
    token = make_secure_token(session['_id'])
    print 'TOKEN'
    print token
    if header_token != token:
        return False
    return True

def error_response(status):
    response = jsonify(error=0)
    response.status_code = status
    return response

if __name__ == '__main__':
    app.run(debug=True)
