import MySQLdb
from itsdangerous import (TimedJSONWebSignatureSerializer 
        as Serializer, BadSignature, SignatureExpired)

BAD_REQUEST = 0
REGISTERED = -1

FAILED = 0
SUCCESS = 1

def connect_db():
    connect = MySQLdb.connect(host   = 'localhost',
                              db     = 'bookmanager',
                              user   = 'root',
                              passwd = 'caraquri')
    connect.cursortall = MySQLdb.cursors.DictCursor
    return connect

def register(db, mail, pswd):
    if mail is '' or pswd is '':
        print 'bad request'
        return BAD_REQUEST
    if getUserByMailAddress(db, mail) is not None:
        print 'registered'
        return REGISTERED

    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    sql = 'insert into users(\
              mail_address,\
              password\
           )values("%s", "%s")' % (mail, pswd)
    cursor.execute(sql)
    db.commit()
    cursor.execute('select count("id") from users')
    id_count = cursor.fetchone()
    return id_count['count("id")']

def login(db, mail, pswd):
    ps = getUserByMailAddress(db, mail)
    print ps
    if ps is not None and ps['password'] == pswd:
        return ps['user_id']
    else:
        return FAILED

def getUserByMailAddress(db, mail):
    cur = db.cursor(MySQLdb.cursors.DictCursor)
    sql = 'select * from users \
           where mail_address = "%s"'\
           % mail
    cur.execute(sql)
    return cur.fetchone()
