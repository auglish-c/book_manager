import MySQLdb
from nose.tools import ok_, eq_
from app.account.users import *

connect = MySQLdb.connect(host='localhost', db = 'test_bookmanager',
                          user='root', passwd='caraquri')
connect.cursorclass = MySQLdb.cursors.DictCursor
cursor = connect.cursor()

def setUp(self):
    print 'setup'

def tearDown(self):
    cursor.execute('TRUNCATE TABLE users')
    cursor.close()
    connect.close()

def test_sign_up():
    cursor.execute('insert into users(user_id, mail_address,password)values(0, "hoge@caraquri", 123)')
    res = register( connect, 'hoge@hoge', '2333' )
    cursor.execute('select * from users')
    ans = ({'mail_address': 'hoge@caraquri', 'password': '123', 'user_id': 0L}, 
           {'mail_address': 'hoge@hoge', 'password': '2333', 'user_id': 1L})
    eq_(cursor.fetchall(), ans)
    eq_(res, 1)
    res = register(connect, 'hoge@hoge', '2333')
    eq_(res, 2)
    res = register(connect, 'hoge@hoge', '')
    eq_(res, 0)

def test_get_Password_by_mail_address():
    userInfo = getPasswordByMailAddress(connect, "hoge@caraquri")
    ans = ({'password': '123'})
    eq_(userInfo, ans)
    userInfo = getPasswordByMailAddress(connect, "hog@caraquri")
    eq_(userInfo, None)

