from flask import Flask,request,render_template
from flask_cors import CORS, cross_origin # 解决本地跨域的问题

app = Flask(__name__)

app.jinja_env.variable_start_string = '%%'
app.jinja_env.variable_end_string = '%%'

@app.route('/')
@cross_origin() # 解决跨域报错
def pag():
    return render_template("pag.html")

@app.route('/test/')
@cross_origin() # 解决跨域报错
def test():
    return render_template("test.html")

@app.route('/sort/')
@cross_origin() # 解决跨域报错
def sort():
    return render_template("sort.html")

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

@app.route('/route/')
@cross_origin() # 解决跨域报错
def route():
    return render_template("route.html")

if __name__ == '__main__':
    app.run()
