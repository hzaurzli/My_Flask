import uuid
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin # 解决本地跨域的问题

# configuration
DEBUG = True
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# enable CORS,解决跨域问题
CORS(app, resources={r'/*': {'origins': '*'}})


app.jinja_env.variable_start_string = '%%'
app.jinja_env.variable_end_string = '%%'

@app.route('/', methods=['get', 'post'])
def home():
    return render_template('index.html')

@app.route('/page_2', methods=['get', 'post'])
def page_2():
    return render_template('page_2.html')

@app.route('/page_3', methods=['get', 'post'])
def page_3():
    return render_template('page_3.html')


@app.route('/table_axios/')
def table_axios():
    data = request.args.to_dict()
    print(data)
    order = data['order']
    curr_page = int(data['curr_page'])
    total_page = int(data['total_page'])
    search = data['search']

    if search == '':
        if (curr_page % 2) == 0:
            rst = {
                "order": order,
                "curr_page": int(curr_page),
                "total_page": int(total_page),
                "data_item": [
                    {
                        'date': '2016-05-03',
                        'name': '王小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-02',
                        'name': '王小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-04',
                        'name': '王小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-01',
                        'name': '王小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-08',
                        'name': '王小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-06',
                        'name': '王小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-07',
                        'name': '王小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }
                ]
            }

        else:
            rst = {
                "order": order,
                "curr_page": int(curr_page),
                "total_page": int(total_page),
                "data_item": [
                    {
                        'date': '2016-05-03',
                        'name': '孙小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-02',
                        'name': '孙小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-04',
                        'name': '孙小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-01',
                        'name': '孙小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-08',
                        'name': '孙小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-06',
                        'name': '孙小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-07',
                        'name': '孙小虎',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }
                ]
            }
    else:
        if (curr_page % 2) == 0:
            rst = {
                "order": order,
                "curr_page": int(curr_page),
                "total_page": int(total_page),
                "data_item": [
                    {
                        'date': '2016-05-03',
                        'name': '王',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-02',
                        'name': '王',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-04',
                        'name': '王',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-01',
                        'name': '王',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-08',
                        'name': '王',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-06',
                        'name': '王',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-07',
                        'name': '王',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }
                ]
            }

        else:
            rst = {
                "order": order,
                "curr_page": int(curr_page),
                "total_page": int(total_page),
                "data_item": [
                    {
                        'date': '2016-05-03',
                        'name': '孙',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-02',
                        'name': '孙',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-04',
                        'name': '孙',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-01',
                        'name': '孙',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-08',
                        'name': '孙',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-06',
                        'name': '孙',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }, {
                        'date': '2016-05-07',
                        'name': '孙',
                        'address': '上海市普陀区金沙江路 1518 弄'
                    }
                ]
            }

    return rst

@app.route('/json/')
@cross_origin() # 解决跨域报错
def json():
    data = request.args.to_dict()
    # dat = data["data"]
    print(data)
    rst = {
    "name":"网站",
    "num":3,
    "sites": [
        { "name":"Google", "info":[ "Android", "Google 搜索", "Google 翻译" ] },
        { "name":"Runoob", "info":[ "菜鸟教程", "菜鸟工具", "菜鸟微信" ] },
        { "name":"Taobao", "info":[ "淘宝", "网购" ] }
    ]
}
    return rst


if __name__ == '__main__':
    app.run()