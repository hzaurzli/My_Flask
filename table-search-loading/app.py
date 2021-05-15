from flask import Flask, render_template, url_for, request
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


@app.route('/', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/<int:page>', methods=['GET', 'POST'])
def index(page):
    page = page
    pages = 5
    # employees = Employees.query.filter().all()
    # employees = Employees.query.paginate(page,pages,error_out=False)
    employees = Employees.query.order_by(Employees.id.asc()).paginate(page, pages, error_out=False)  # desc()
    if request.method == 'POST' and 'tag' in request.form:
        tag = request.form["tag"]
        search = "%{}%".format(tag)
        time.sleep(10)
        employees = Employees.query.filter(
            or_(Employees.fullname.like(search), Employees.position.like(search), Employees.office.like(search),
                Employees.age.like(search), Employees.startdate.like(search), Employees.salary.like(search))).paginate(
            per_page=pages, error_out=False)

        return render_template('index.html', employees=employees, tag=tag)
    return render_template('index.html', employees=employees)


if __name__ == '__main__':
    app.run(debug=True)