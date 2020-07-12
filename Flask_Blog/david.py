from flask import Flask,render_template,request,redirect,url_for,session,flash
import config
from models import User,Question,Comment
from exts import db
from decoration import login_required
from sqlalchemy import or_


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
#db = pymysql.connect("127.0.0.1", "root", "sky15887182979", "david")
#db.create_all()


@app.route("/")
def index():
    context = {
        'questions' : Question.query.order_by(Question.create_time.desc()).all()
    }
    return render_template('index.html',**context)


@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        phone = request.form.get("phonenumber")
        password = request.form.get("password")
        user = User.query.filter(User.phone == phone,
                                 User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'Account error'

@app.route("/regist/",methods=["GET","POST"])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        username = request.form.get("yourname")
        phone = request.form.get("phonenumber")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user = User.query.filter(User.phone == phone).first()
        if user:
            return u'Signed'
        else:
            if password1 != password2:
                return u'error password'
            else:
                user = User(phone=phone,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/question/',methods=['GET','POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get("title")
        content = request.form.get("content")
        question = Question(title=title,content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))

@app.route("/question_del/<question_id>")
def question_del(question_id):
    question = Question.query.get(question_id)
    if question:
        try:
            Comment.query.filter_by(question_id=question.id).delete()
            db.session.delete(question)
            db.session.commit()
        except Exception as e:
            print(e)
            flash("Error")
            db.session.rollback()
    else:
        flash("No")
    return redirect(url_for('index'))

@app.route("/detail/<question_id>/")
def detail(question_id):
    question_model = Question.query.filter(Question.id==question_id).first()
    return render_template('detail.html',question=question_model)

@app.route('/add_comment/',methods=["POST"])
@login_required
def add_comment():
    content = request.form.get('comment-content')
    question_id = request.form.get('question_id')
    comment = Comment(content=content)
    user_id = session["user_id"]
    user = User.query.filter(User.id==user_id).first()
    comment.author = user
    question = Question.query.filter(Question.id == question_id).first()
    comment.question = question
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('detail',question_id=question_id))

@app.route("/comment_del/<comment_id>")
def comment_del(comment_id):
    comment = Comment.query.get(comment_id)
    if comment:
        try:
            db.session.delete(comment)
            db.session.commit()
        except Exception as e:
            print(e)
            flash("Error")
            db.session.rollback()
    else:
        flash("No")
    return redirect(url_for('index'))

@app.route('/search/')
def search():
    q = request.args.get('q')
    questions = Question.query.filter(or_(Question.title.contains(q),
                              Question.content.contains(q)))
    return render_template('index.html',questions=questions)


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user_id:
            return {'user':user}
    return {}


if __name__ == '__main__':
    app.run()