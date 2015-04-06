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

def test_login():
    cursor.execute('insert into users(user_id, mail_address,password)values(1, "hoge@caraquri", 123)')
    ok_(login( connect, 'hoge@caraquri', '123' ))
