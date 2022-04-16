from flask import Flask,render_template,flash,request
import time

app = Flask(__name__)

app.secret_key = '123456'


@app.route('/')
def test():
    aa = 'tes'
    return render_template("test.html",aa=aa)

@app.route('/index/')
def index():
    flash("lllll")
    time.sleep(2)
    return render_template("index.html")

@app.route('/pag/')
def pag():
    aa = request.args.to_dict()
    print(aa)

    return render_template("ajax.html")

@app.route('/ajax/')
def ajax():
    rst =  { "first": [
  		{ "name": "张三", "sex": "男"},
        { "name": "李思", "sex": "女"},
        { "name": "王五", "sex": "男"},
        { "name": "赵柳", "sex": "女"}] }
    time.sleep(5)
    return rst

@app.route('/spi/')
def spi():
    return render_template("spicies.html")

@app.route('/ppp/<spicies>/<tissue>')
def ppp(spicies,tissue):
    aa = spicies
    bb = tissue
    print(aa)
    print(bb)
    rst = {"aa": aa,"bb": bb}
    return rst

@app.route('/sp/<spicies>/<tissue>')
def sp(spicies,tissue):
    return render_template("sp.html",sp=spicies,ti=tissue)

@app.route('/down/')
def down():
    return render_template("download.html")

@app.route('/download/')
def download():
    rst = "money"
    with open("D:/pycharm/jquery_hide_window/static/jest.txt", "w") as w:
        line = rst + "\n"
        w.write(line)

    file = "/static/jest.txt"

    return file


@app.route('/param/',methods=['GET'])
def param():
    if request.method == "GET":
        data = request.args.get("data")
        print(data)
        return data

@app.route('/par/')
def par():
    return render_template("param.html")


@app.route('/sel/')
def sel():
    return render_template("select.html")

@app.route('/ind/')
def ind():
    return render_template("ind.html")

@app.route('/select/',methods=['GET'])
def select():
    if request.method == "GET":
        data = request.args.to_dict()
        print(type(data))
        dat = data["fname"]
        print(dat)
        return dat


@app.route('/div/', methods=['GET'])
def div():
    return render_template("div.html")

@app.route('/div_test/', methods=['GET'])
def div_test():
    rst = "<p>hhhhahah</p>"
    return rst

@app.route('/pagtion/')
def pagtion():
    return render_template("pag.html")

@app.route('/pag_ajax/', methods=['GET'])
def pag_ajax():
    data = request.args.to_dict()
    dat = data["data"]
    print(dat)
    skip = 1
    mm = [{ "name": "张三", "sex": "男"},
        { "name": "李思", "sex": "女"},
        { "name": "王五", "sex": "男"},
        { "name": "赵柳", "sex": "女"}]
    nn = mm[int(dat)-1 : int(dat)-1 + skip]
    rst = {}
    rst["first"] = nn
    time.sleep(3)
    return rst

@app.route('/pag_ajax_count/', methods=['GET'])
def pag_ajax_count():
    data = request.args.to_dict()
    dat = data["data"]
    print(dat)
    if dat == '1':
        mm = 100
    else:
        mm = 1000
    rst = {}
    rst["first"] = mm
    time.sleep(3)
    return rst

@app.route('/attr/')
def attr():
    return render_template("pag_A.html")

@app.route('/attr_B/')
def attr_B():
    return render_template("pag_B.html")

@app.route('/gene/')
def gene():
    return render_template("gene_struction.html")

@app.route('/check/')
def check():
    return render_template("checkbox.html")

@app.route('/progre/')
def progre():
    return render_template("progress.html")

@app.route('/igv/')
def igv():
    return render_template("igv.html")

@app.route('/jq/')
def jq():
    return render_template("jqval.html")

@app.route('/syn/')
def syn():
    return render_template("SYNVISIO.html")

@app.route('/tab/')
def tab():
    return render_template("tab.html")
#
# @app.route("/upload",methods=['GET','POST'])
# def upload():
#     if request.method=='POST':
#         f = request.files["file"]
#         stream = f.stream
#         url = 'https://synvisio.github.io/#/Upload'
#         fields = {"category": "1", "refKey": "WX"}
#         files = {'file': (f.filename, stream)}
#         r = requests.post(url, data=fields, verify=False, files=files)
#     return r

@app.route('/chart/')
def chart():
    return render_template("chart.html")

@app.route('/chart_json/', methods=['GET'])
def chart_json():
    rst = {
        "reDates":[
            {
                "ChartName":"2010 ~ 2016 年太阳能行业就业人员发展情况","XAxisName":["Feb","Mar","W01","W02","W03","W04"],
                "DataList":[{"name":"安装，实施人员","data":[8000,4000,8000,6000,5000,4000]},
                            {"name":"工人","data":[8000,5000,8000,8000,6000,5000]},
                            {"name":"销售","data":[5000,8000,4000,8000,8000,8000]}
                            ]
            },
            {
                "ChartName":"美苏核武器库存量","XAxisName":["Feb","Mar","W01","W02","W03","W04"],
                "DataList":[{"name":"美国","data":[3000,4000,8000,6000,5000,4000]},
                            {"name":"苏联/俄罗斯","data":[8000,5000,8000,8000,6000,5000]},
                            {"name":"其他","data":[5000,8000,4000,8000,8000,8000]}
                            ]
            }
        ]
    }

    return rst


if __name__ == '__main__':
    app.run()
