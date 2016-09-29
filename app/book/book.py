import MySQLdb
from datetime import date
import pprint
import json
import urllib
import urllib2

def connect_db():
    connect = MySQLdb.connect(host = 'localhost',
                              db = 'bookmanager',
                              user = 'root',
                              passwd = 'caraquri')
    connect.cursortall = MySQLdb.cursors.DictCursor
    return connect

def register(db, data):
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('select count("id") from books')
    id_count = cursor.fetchone()
    if id_count['count("id")'] == 0l:
        new_id = 0
    else:
        new_id = int(id_count['count("id")'])
    today = date.today()
    image_url = image_upload(data['image_data'])
    sql = 'insert into books(\
              id,\
              user_id,\
              name,\
              price,\
              purchase_date,\
              image_url\
           )values(%d, %d, "%s", "%s", "%s", "%s")'\
           % (new_id, data['user_id'], data['name'], data['price'],
              data['purchase_date'], image_url)
    cursor.execute(sql)
    db.commit()
    return new_id

def update(db, book_id, data):
    image_url = image_upload(data['image_data'])
    cur = db.cursor(MySQLdb.cursors.DictCursor)
    sql = 'update books set name = "%s",\
                            price = "%s",\
                            purchase_date = "%s",\
                            image_url = "%s"\
                        where id = "%s"' %\
          (data['name'], data['price'], data['purchase_date'],
           image_url, book_id)
    cur.execute(sql)
    db.commit()
    return book_id

def get(db, page, user_id):
    cur = db.cursor(MySQLdb.cursors.DictCursor)
    pages = page.split('-')
    pages[1] = str(int(pages[0]) + int(pages[1]) - 1)
    sql = 'select id, image_url, name, price, purchase_date \
           from books\
           where user_id = %s and id between %s and  %s' %\
           (user_id, pages[0], pages[1])
    cur.execute(sql)
    return cur.fetchall()

def image_upload(img_data):
    value = {'image' : img_data}
    url = "http://api.imgur.com/3/image"
    header = {'Authorization' : 'Client-ID 195c2aaa51fa976'}

    data = urllib.urlencode(value)
    req = urllib2.Request(url, data, url)
    res = urllib2.urlopen(req)
    resJson = json.load(res.road())
    return resJson['data']['link']
