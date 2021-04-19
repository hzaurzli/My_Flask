from flask import Flask, render_template, url_for, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
import time

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


@app.route("/")
def mm():
    return render_template("BASE.html")


@app.route('/aaa')
def index():
    page = int(request.args["page"])
    limit = int(request.args["limit"])

    result = Employees.query.order_by(Employees.id.asc()).all()
    alldata = []
    data = {}
    for one in result:
        data = {"id": one.id, "fullname": one.fullname, "position": one.position,
                "office": one.office, "age": one.age, "startdate": one.startdate,
                "salary": one.salary}
        alldata.append(data)
        # alldata["id"] = Employees.id
        # alldata["fullname"] = Employees.fullname
        # alldata["position"] = Employees.position
        # alldata["office"] = Employees.office
        # alldata["age"] = Employees.age
        # alldata["startdate"] = Employees.startdate
        # alldata["salary"] = Employees.salary

    aaa = {"code": 0, "msg": ""}
    aaa["data"] = alldata
    aaa["count"] = len(aaa["data"])
    aaa["data"] = aaa["data"][(page - 1) * 10: (page - 1) * 10 + limit]
    import json
    rst = make_response(json.dumps(aaa))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    print(rst)
    return rst

if __name__ == '__main__':
    app.run(debug=True)

