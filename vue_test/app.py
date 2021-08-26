from flask import Flask,request,render_template

app = Flask(__name__)

app.jinja_env.variable_start_string = '%%'
app.jinja_env.variable_end_string = '%%'

@app.route('/')
def pag():
    return render_template("pag.html")

@app.route('/test/')
def test():
    return render_template("test.html")

@app.route('/sort/')
def sort():
    return render_template("sort.html")

@app.route('/json/')
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
def route():
    return render_template("route.html")

if __name__ == '__main__':
    app.run()
