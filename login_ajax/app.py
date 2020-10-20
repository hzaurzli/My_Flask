from flask import Flask, render_template, request, url_for, json
from flask_mysqldb import MySQL, MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "caircocoders-ednalan-2020"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sky15887182979'
app.config['MYSQL_DB'] = 'flaskdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    # validate the received values
    if _name and _email and _password:

        # All Good, let's call MySQL
        cur = mysql.connection.cursor()
        _hashed_password = generate_password_hash(_password)
        cur.execute("INSERT INTO users (name, email, password) VALUES (%s,%s,%s)", (_name, _email, _hashed_password,))
        data = cur.fetchall()

        if len(data) is 0:
            mysql.connection.commit()
            return json.dumps(
                {'message': 'User created successfully !'})  # json.dumps() takes in a json object and returns a string.
        else:
            return json.dumps({'error': str(data[0])})
    else:
        x = '{ "html":"<b>Enter the required fields</b>"}'
        y = json.loads(x)  # json.loads() takes in a string and returns a json object.
        return y["html"]


if __name__ == '__main__':
    app.run(debug=True)