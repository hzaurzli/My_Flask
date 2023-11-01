from random import choice
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.jinja_env.variable_start_string = '%%'
app.jinja_env.variable_end_string = '%%'

@app.route('/jsondata', methods=['POST', 'GET'])
def infos():
   rst = {
  "data": [
    {
      "id": "1",
      "name": "Tiger Nixon",
      "office": "[{value:135, name:'b2'},{value:374,name:'b3'},{value:600,name:'b4'}]",
      "salary": "$320,800",
      "start_date": "2011/04/25",
      "extn": "5421"
    },
    {
      "id": "2",
      "name": "Garrett Winters",
      "office": "[{value:235, name:'a2'},{value:274,name:'a3'},{value:400,name:'a4'}]",
      "salary": "$170,750",
      "start_date": "2011/07/25",
      "extn": "8422"
    },
    {
      "id": "3",
      "name": "David py",
      "office": "[{value:635, name:'c2'},{value:2245,name:'c3'},{value:800,name:'c4'}]",
      "salary": "$530,750",
      "start_date": "2018/07/21",
      "extn": "8999"
    }
  ]
}
   return rst


@app.route('/')
def hi():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()