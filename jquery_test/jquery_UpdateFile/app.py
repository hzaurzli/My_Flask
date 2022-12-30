from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        if f.filename != None:
            f.save(f.filename)
            return render_template('index.html')
        else:
            return render_template('index.html')


@app.route('/up_file', methods=['GET', 'POST'])
def up_file():
    if request.method == "POST":
        file = request.files['file']
        file_name = file.filename
        file.save(os.path.join('templates\\files', file_name))

        return '上传成功'

if __name__ == '__main__':
    app.run(debug=True)