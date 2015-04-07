import MySQLdb
from nose.tools import ok_, eq_
from app.book.book import *
from datetime import datetime as dt
from decimal import *
import pprint

connect = MySQLdb.connect(host='localhost', db = 'test_bookmanager',
                          user='root', passwd='caraquri')
connect.cursorclass = MySQLdb.cursors.DictCursor
cursor = connect.cursor()

def setUp(self):
    print 'setup'

def tearDown(self):
    cursor.execute('TRUNCATE TABLE books')
    cursor.execute('TRUNCATE TABLE users')
    cursor.close()
    connect.close()

def test_regist():
    cursor.execute('insert into users(user_id, mail_address,password)values(0, "hoge@caraquri", 123)')
    eq_( register(connect, 1, data0), 0)

def test_update():
    eq_(update(connect, 0, data), 0)
    

def test_get():
    for i in range(0, 10):
        register(connect, 1, data1[i])
    data1.insert(0, data)
    ans = tuple(data1)
    result = get(connect, "0-1")
    eq_(result[0]['name'], data['name'])
    eq_(result[0]['purchase_date'], dt.strptime(data['purchase_date'], '%Y-%m-%d'))
    eq_(result[0]['image_url'], data['image_url'])
    eq_(result[0]['price'], Decimal(data['price']))
    result = get(connect, "1-10")
    eq_(result[0]['name'], data1[1]['name'])
    eq_(result[0]['purchase_date'], dt.strptime(data1[1]['purchase_date'], '%Y-%m-%d'))
    eq_(result[0]['image_url'], data1[1]['image_url'])
    eq_(result[0]['price'], Decimal(data1[1]['price']))
    eq_(result[-1]['name'], data1[10]['name'])
    eq_(result[-1]['purchase_date'], dt.strptime(data1[10]['purchase_date'], '%Y-%m-%d'))
    eq_(result[-1]['image_url'], data1[10]['image_url'])
    eq_(result[-1]['price'], Decimal(data1[10]['price']))

data0 = {'image_url': '/O3sTJD_h_400x400.jpeg',
        'name': 'dog & mikan',
        'price': '3000',
        'purchase_date': '2016-11-11'}
data = { 'image_url': '/O3sTJD_h_400x400.jpeg',
        'name': 'cat & banana',
        'price': '30000',
        'purchase_date': '2016-11-23'}

data1 = [{'image_url': '/O3sTJD_h_400x400.jpeg',
         'name': 'dog & mikan vol1',
         'price': '3000',
         'purchase_date': '2016-11-11'},
        {'image_url': '/O3sTJD_h_400x400.jpeg',
         'name': 'dog & mikan vol2',
         'price': '3000',
         'purchase_date': '2016-11-12'},
        {'image_url': '/O3sTJD_h_400x400.jpeg',
         'name': 'dog & mikan vol3',
         'price': '3000',
         'purchase_date': '2016-11-13'},
        {'image_url': '/O3sTJD_h_400x400.jpeg',
         'name': 'dog & mikan vol4',
         'price': '3000',
         'purchase_date': '2016-11-14'},
        {'image_url': '/O3sTJD_h_400x400.jpeg',
         'name': 'dog & mikan vol5',
         'price': '3000',
         'purchase_date': '2016-11-14'},
        {'image_url': '/O3sTJD_h_400x400.jpeg',
         'name': 'dog & mikan vol6',
         'price': '3000',
         'purchase_date': '2016-11-14'},
        {'image_url': '/O3sTJD_h_400x400.jpeg',
         'name': 'dog & mikan vol7',
         'price': '3000',
         'purchase_date': '2016-11-15'},
        {'image_url': '/O3sTJD_h_400x400.jpeg',
         'name': 'dog & mikan vol8',
         'price': '3000',
         'purchase_date': '2016-11-16'},
        {'image_url': '/O3sTJD_h_400x400.jpeg',
         'name': 'dog & mikan vol9',
         'price': '3000',
         'purchase_date': '2016-11-17'},
        {'image_url': '/O3sTJD_h_400x400.jpeg',
         'name': 'dog & mikan vol10',
         'price': '3000',
         'purchase_date': '2016-11-17'}]
