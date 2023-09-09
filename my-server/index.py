from flask import Flask,jsonify
from collections import  Counter
import pymysql

app = Flask(__name__)
connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     database='crawling',
                                     cursorclass=pymysql.cursors.DictCursor)

@app.route("/api")
def hello_world():
    cursor = connection.cursor()
    sql = "select * from crawling"
    cursor.execute(sql)
    result = cursor.fetchall()
    return jsonify(result)

@app.route("/api2")
def api2():
    cursor = connection.cursor()
    sql = "select * from crawling1"
    cursor.execute(sql)
    result = cursor.fetchall()
    return jsonify(result)

@app.route("/view_skill")
def view_skill():
    # 把所有的skill的数据取出来
    cursor = connection.cursor()
    sql = "select skill from crawling"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

    # 1. 先把字典格式转成列表形式
    a=[item.get('skill') for item in result]
    print(a)
    b=[item.split(",") for item in a]
    print(b)
    c=[]
    for item in b:
       c+=item
    print(c)
    result=Counter(c)
    result=result.most_common()[:10]
    skillname=[item[0] for item in result]
    skilldata=[item[1] for item in result]
    return jsonify([skillname,skilldata])

@app.route("/python_skill")
def python_skill():
    # 把所有的skill的数据取出来
    cursor = connection.cursor()
    sql = "select skill from crawling1"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

    # 1. 先把字典格式转成列表形式
    a=[item.get('skill') for item in result]
    print(a)
    b=[item.split(",") for item in a]
    print(b)
    c=[]
    for item in b:
       c+=item
    print(c)
    result=Counter(c)
    result=result.most_common()[:10]
    skillname=[item[0] for item in result]
    skilldata=[item[1] for item in result]
    return jsonify([skillname,skilldata])
app.run()