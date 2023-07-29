#  -*- UTF-8 -*- #
"""
@filename:db_storage.py
@author:Anza
@time:2023-07-28
"""


import pymysql


def login():
    username = 'root'
    pwd = '123456'
    host = 'localhost'
    db = 'spiders'
    port = 3306

    db = pymysql.connect(host=host, user=username, password=pwd,
                         port=port, db=db)
    return db


def mysql_build():
    db = login()
    cursor = db.cursor()
    # cursor.execute('SELECT VERSION()')
    # data = cursor.fetchone()
    # print("DATA V:", data)
    # cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')
    sql = 'CREATE TABLE IF NOT EXISTS students' \
          '(id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL,' \
          'age INT NOT NULL, PRIMARY KEY (id))'
    cursor.execute(sql)
    db.close()


def mysql_insert():
    db = login()
    id = '20120001'
    user = 'Bob'
    age = 20

    cursor = db.cursor()
    sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
    try:
        cursor.execute(sql, (id, user, age))
        db.commit()
    except:
        db.rollback()
    db.close()

    # dynamic_writing
    # data = {
    #     'id': '20120001',
    #     'name': 'Bob',
    #     'age': 20
    # }
    # table = 'students'
    # keys = ', '.join(data.keys())
    # values = ', '.join(['%s']*len(data))
    # sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,
    #                                                              keys=keys,
    #                                                              values=values)
    # try:
    #     if cursor.execute(sql, tuple(values)):
    #         print("successful!")
    #         db.commit()
    # except:
    #     print('Failed')
    #     db.rollback()
    # db.close()

def mysql_update():
    db = login()
    cursor = db.cursor()

    sql = 'UPDATE students SET age = %s WHERE name = %s'
    try:
        cursor.execute(sql, (25, 'Bob'))
        db.commit()
    except:
        db.rollback()
    db.close()


def mysql_delete():
    db = login()
    cursor = db.cursor()

    table = 'students'
    condition = 'age > 20'

    sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table,
                                                         condition=condition)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def mysql_select():
    db = login()
    cursor = db.cursor()

    sql = 'SELECT * FROM students WHERE age >= 20'
    try:
        cursor.execute(sql)
        print('Count: ', cursor.rowcount)
        row = cursor.fetchone()
        while row:
            print('Row: ', row)
            row = cursor.fetchone()
    except:
        print('Error')
    db.close()

if __name__ == '__main__':
    # mysql_build()
    # mysql_insert()
    # mysql_update()
    mysql_select()
