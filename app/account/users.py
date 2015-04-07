import MySQLdb

def connect_db():
    connect = MySQLdb.connect(host   = 'localhost',
                              db     = 'bookmanager',
                              user   = 'root',
                              passwd = 'caraquri')
    connect.cursortall = MySQLdb.cursors.DictCursor
    return connect

def register(db, mail, pswd):
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
    cur = db.cursor(MySQLdb.cursors.DictCursor)
    sql = 'select password from users \
           where mail_address = "%s"'\
           % mail
    cur.execute(sql)
    ps = cur.fetchone()
    if ps['password'] == pswd:
        return 1
    else:
        return 0
