import MySQLdb
from datetime import date
import pprint
import json

def connect_db():
    connect = MySQLdb.connect(host = 'localhost',
                              db = 'bookmanager',
                              user = 'root',
                              passwd = 'caraquri')
    connect.cursortall = MySQLdb.cursors.DictCursor
    return connect

def regist(db, user_id, data):
    cursor = db.cursor()
    cursor.execute('select count("id") from books')
    id_count = cursor.fetchone()
    new_id = int(id_count['count("id")']) + 1
    today = date.today()
    sql = 'insert into books(\
              id,\
              user_id,\
              name,\
              price,\
              purchase_date,\
              image_url\
           )values(%d, %d, "%s", "%s", "%s", "%s")'\
           % (new_id, user_id, data['name'], data['price'],
              data['purchase_date'], data['image_url'])
    cursor.execute(sql)
    db.commit()
    return new_id
    
def update(db, book_id,data):
    cur = db.cursor()
    sql = 'update books set name = "%s",\
                            price = "%s",\
                            purchase_date = "%s",\
                            image_url = "%s"\
                        where id = "%s"' %\
          (data['name'], data['price'], data['purchase_date'],
           data['image_url'], book_id)
    cur.execute(sql)
    return book_id

def get(db, page):
    cur = db.cursor()
    pages = page.split('-')
    sql = 'select id, image_url, name, price, purchase_date \
           from books\
           where id between %s and  %s' %\
           (pages[0], pages[1])
    cur.execute(sql)
    return cur.fetchall()
    #pprint.pprint( cur.fetchall())

