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


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150))
    position = db.Column(db.String(150))
    office = db.Column(db.String(150))
    age = db.Column(db.Integer)
    startdate = db.Column(db.String(150))
    salary = db.Column(db.String(150))


def Dynamic_programming(seq_1,seq_2):
    A = np.ones([5, 5], dtype=np.int16) * -2 + np.eye(5, dtype=np.int16) * 5
    A[0, 0] = 0
    name_list = ["_", "A", "C", "G", "T"]
    punish_matrix = pd.DataFrame(A, columns=name_list, index=name_list)

    str_one = seq_1
    str_two = seq_2
    s1 = ''
    s2 = ''

    index = ["_"] + [i for i in str_one]
    columns = ["_"] + [i for i in str_two]
    score_matrix = pd.DataFrame(np.zeros([len(str_one) + 1, len(str_two) + 1]), index=index, columns=columns)

    punish = -3
    for i in range(len(str_one) + 1):
        for j in range(len(str_two) + 1):
            if i == 0 or j == 0:
                score_matrix.iloc[i, j] = 0 + punish * i + punish * j
            else:
                insert = score_matrix.iloc[i, j - 1] + punish
                delect = score_matrix.iloc[i - 1, j] + punish
                match = score_matrix.iloc[i - 1, j - 1] + punish_matrix.loc[str_one[i - 1], str_two[j - 1]]
                score_matrix.iloc[i, j] = max(insert, delect, match)

    i = len(str_one)
    j = len(str_two)

    while (i > 0 or j > 0):
        if (i > 0 and j > 0 and score_matrix.iloc[i, j] == score_matrix.iloc[i - 1, j - 1] + punish_matrix.loc[
            str_one[i - 1], str_two[j - 1]]):
            s1 += str_one[i - 1]
            s2 += str_two[j - 1]
            i -= 1
            j -= 1
        elif (j > 0 and score_matrix.iloc[i, j] == score_matrix.iloc[i, j - 1] + punish):
            s1 += '-'
            s2 += str_two[j - 1]
            j -= 1
        elif (i > 0 and score_matrix.iloc[i, j] == score_matrix.iloc[i - 1, j] + punish):
            s1 += str_one[i - 1]
            s2 += '-'
            i -= 1

    #return(score_matrix)
    return(s1[::-1] + '\n' + s2[::-1])


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/page_1/',methods=["GET"])
def page_1():
    return render_template("page_1.html")


@app.route('/page_2/', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/page_2/<int:page>', methods=['GET', 'POST'])
def page_2(page):
    page = page
    pages = 10
    # employees = Employees.query.filter().all()
    # employees = Employees.query.paginate(page,pages,error_out=False)
    employees = Employees.query.order_by(Employees.id.asc()).paginate(page, pages, error_out=False)
    if request.method == 'POST' and 'tag' in request.form:
        tag = request.form["tag"]
        search = "%{}%".format(tag)
        employees = Employees.query.filter(
            or_(Employees.fullname.like(search), Employees.position.like(search), Employees.office.like(search),
                Employees.age.like(search), Employees.startdate.like(search), Employees.salary.like(search))).paginate(
            per_page=pages, error_out=False)
        list = Employees.query.filter(
            or_(Employees.fullname.like(search), Employees.position.like(search), Employees.office.like(search),
                Employees.age.like(search), Employees.startdate.like(search), Employees.salary.like(search))).all()
        #print(employees)
        time.sleep(5)
        if len(list) != 0:
            return render_template('page_2.html', employees=employees, tag=tag)
        else:
            return render_template('page_3.html')

    if request.method == 'POST' and 'age_min' and 'age_max' in request.form:
        age_min = request.form["age_min"]
        age_max = request.form["age_max"]
        employees = Employees.query.filter(Employees.age > age_min, Employees.age < age_max).paginate(per_page=pages, error_out=True)
        return render_template('page_2.html', employees=employees, age_min=age_min,age_max=age_max)
    return render_template('page_2.html', employees=employees)

@app.route('/page_3/')
def page_3():
    return render_template("page_3.html")


@app.route('/page_5/<string:fullname>', methods=['GET', 'POST'])
def page_5(fullname):
    myids = Employees.query.filter(Employees.fullname == fullname).paginate(per_page= 1, error_out=False)
    print(myids)
    return render_template("page_5.html",myids=myids)

@app.route('/page_6/', methods=['GET', 'POST'])
def page_6():
    if request.method == 'POST' and 'seq_1' and 'seq_2' in request.form:
        seq_1 = request.form["seq_1"]
        seq_2 = request.form["seq_2"]
        result = Dynamic_programming(seq_1, seq_2)
        return render_template("result.html",result=result,seq_1=seq_1,seq_2=seq_2)
    return render_template("wait.html")

if __name__ == '__main__':
    app.run()
