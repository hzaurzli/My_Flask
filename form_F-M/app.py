from flask import Flask
from flask import request
from flask import render_template
from flask import redirect


USERS = {
    'tom': {'gender': 'male', 'chinese': 90, 'math': 78},
    'bob': {'gender': 'male', 'chinese': 87, 'math': 65},
    'lucy': {'gender': 'female', 'chinese': 74, 'math': 73},
    'lily': {'gender': 'female', 'chinese': 86, 'math': 90},
    'alex': {'gender': 'male', 'chinese': 91, 'math': 77},
    'john': {'gender': 'male', 'chinese': 79, 'math': 72},
    'jack': {'gender': 'male', 'chinese': 60, 'math': 99},
    'tomas': {'gender': 'male', 'chinese': 88, 'math': 98},
    'eva': {'gender': 'female', 'chinese': 100, 'math': 85},
    'ella': {'gender': 'female', 'chinese': 70, 'math': 81},
}

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', users=USERS)


@app.route('/modify', methods=('GET', 'POST'))
def modify():
    if request.method == 'POST':
        global USERS
        name = request.form['name']
        USERS[name]['gender'] = request.form['gender']
        USERS[name]['chinese'] = int(request.form['chinese'])
        USERS[name]['math'] = int(request.form['math'])
        return redirect('/')
    else:
        name = request.args['name']
        info = USERS[name]
        return render_template('modify.html', name=name, info=info)



if __name__ == '__main__':
    app.debug = True
    app.run()