from flask import Flask,render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pymysql

app = Flask(__name__)

class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:sky15887182979@127.0.0.1:3306/book"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "doiso7fd89fyd9^(fsd"


app.config.from_object(Config)
db = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = "tbl_authors"
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    books = db.relationship("Book",backref="author")


class Book(db.Model):
    __tablename__ = "tbl_books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))

class AuthorBookForm(FlaskForm):
    author_name = StringField(label=u"author", validators=[DataRequired(u"作者必填")])
    book_name = StringField(label=u"book", validators=[DataRequired(u"书籍必填")])
    submit = SubmitField(label=u"save")


@app.route("/", methods=["GET","POST"])
def index():
    form = AuthorBookForm()
    if form.validate_on_submit():
        author_name = form.author_name.data
        book_name = form.book_name.data
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name, author_id=author.id)
        db.session.add(book)
        db.session.commit()

    author_li = Author.query.all()
    return render_template("author_book.html", authors=author_li,form=form)

@app.route("/delete_book",methods=["POST"])
def delete_book():
    req_dict = request.get_json()
    book_id = req_dict.get("book_id")

    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify(code=0, message="OK")

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # au_xi = Author(name='xihongshi')
    # au_qian = Author(name='xiaoqian')
    # au_san = Author(name='tangjiasanshao')
    # db.session.add_all([au_xi,au_qian,au_san])
    # db.session.commit()
    #
    # bk_xi = Book(name='tunshi',author_id=au_xi.id)
    # bk_xi2 = Book(name='cunmang', author_id=au_xi.id)
    # bk_qian = Book(name='piaomiao', author_id=au_qian.id)
    # bk_san = Book(name='binghuo', author_id=au_san.id)
    # db.session.add_all([bk_xi, bk_xi2, bk_qian, bk_san])
    # db.session.commit()
    app.run(debug=True)