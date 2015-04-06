import MySQLdb

def connect_db():
    connect = MySQLdb.connect(host = 'localhost',
                              db = 'bookmanager',
                              user = 'root',
                              passwd = 'caraquri')
    connect.cursortall = MySQLdb.cursors.DictCursor
    return connect

def signup(db, mail, pswd):
    cursor = db.cursor()
    cursor.execute('select count("id") from users')
    id_count = cursor.fetchone()
    new_id = int(id_count['count("id")']) + 1
    sql = 'insert into users(\
              user_id,\
              mail_address,\
              password\
           )values(%d, "%s", %s)' % (new_id, mail, pswd)
    cursor.execute(sql)
    db.commit()

def login(db, mail, pswd):
    cur = db.cursor()
    sql = 'select password from users \
           where mail_address = "%s"'\
           % mail
    cur.execute(sql)
    ps =  cur.fetchone()
    print ps['password']
    if ps['password'] == pswd:
        return 1
    else:
        return 0
