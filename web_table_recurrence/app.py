from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def pvuv():
    data = []
    with open("D:\c\pvuv.txt") as f:
        for i in f:
            i = i[:-1]
            u1,u2,u3,u4,u5 = i.split("\t")
            data.append([u1, u2, u3, u4, u5])

    return render_template("pvuv.html",data=data)

if __name__ == '__main__':
    app.run()