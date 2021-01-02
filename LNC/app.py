from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

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
        print(employees)
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

if __name__ == '__main__':
    app.run()
