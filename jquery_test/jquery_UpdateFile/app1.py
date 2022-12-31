from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/up_file', methods=['GET', 'POST'])  # 接受并存储文件
def up_file():
    if request.method == "POST":
        # obtain file
        f = request.files['file']
        print(f.filename)
        f.save(f.filename)
        return 'Upload successful'


@app.route('/', methods=['get', 'post'])
def index():
    return render_template('upload.html')


if __name__ == "__main__":
    app.run()