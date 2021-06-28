from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import time
import numpy as np
import pandas as pd
import argparse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
# app.config['SECRET_KEY'] = 'cairocoders-ednalan'

db = SQLAlchemy(app)

# app.jinja_env.variable_start_string = '%%'
# app.jinja_env.variable_end_string = '%%'


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150))
    position = db.Column(db.String(150))
    office = db.Column(db.String(150))
    age = db.Column(db.Integer)
    startdate = db.Column(db.String(150))
    salary = db.Column(db.String(150))


@app.route('/', methods=['POST', 'GET'])
def search():
    if request.method == 'POST' and 'tag' in request.form:
        tag = request.form["tag"]
        return render_template("index.html",tag=tag)
    return render_template("add.html")

@app.route('/jsondata/<tag>', methods=['POST', 'GET'])
def infos(tag):
    # exp = Employees.query.order_by(Employees.id.asc())
    exp = Employees.query.filter(
        or_(Employees.fullname == tag))
    alldata = []
    data = {}
    for one in exp:
        data = {"id": one.id, "fullname": one.fullname, "position": one.position,
                "office": one.office, "age": one.age, "startdate": one.startdate,
                "salary": one.salary}
        alldata.append(data)

    rst = {}
    rst["data"] = alldata
    print(rst)
    return rst

if __name__ == '__main__':
    app.run()