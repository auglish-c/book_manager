import MySQLdb

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
        return 0
    if getPasswordByMailAddress(db, mail) is not None:
        print 'registered'
        return 2

    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('select count("id") from users')
    id_count = cursor.fetchone()
    if id_count['count("id")'] == 0L:
        new_id = 0
    else:
        new_id = int(id_count['count("id")'])
    sql = 'insert into users(\
              user_id,\
              mail_address,\
              password\
           )values(%d, "%s", "%s")' % (new_id, mail, pswd)
    cursor.execute(sql)
    db.commit()
    return 1

def login(db, mail, pswd):
    ps = getPasswordByMailAddress(db, mail)
    print ps
    if ps['password'] == pswd:
        return 1
    else:
        return 0

def getPasswordByMailAddress(db, mail):
    cur = db.cursor(MySQLdb.cursors.DictCursor)
    sql = 'select password from users \
           where mail_address = "%s"'\
           % mail
    cur.execute(sql)
    return cur.fetchone()
