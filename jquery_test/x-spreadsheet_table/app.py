import json, csv
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin # 解决本地flask跨域问题

app = Flask(__name__)

app.jinja_env.variable_start_string = '%%'
app.jinja_env.variable_end_string = '%%'


@app.route('/greet', methods=['GET', 'POST'])
@cross_origin() # 解决本地flask跨域问题
def greet():
    if request.method == 'GET':
        name = request.args.to_dict()
        print(name)
        list_all = []
        lis_r = []
        lis_c = []
        for key in name:
            key_all = key.replace('name[','').replace(']','')
            key_r = key_all.split('_')[0]
            key_c = key_all.split('_')[1]
            lis_r.append(key_r)
            lis_c.append(key_c)
            lis_r = list(set(lis_r))
            lis_c = list(set(lis_c))
        max_r = max(lis_r)
        max_c = max(lis_c)

        print(max_r)
        print(max_c)

        for n in range(0,int(max_r) + int(1)):
            dic_c = {}
            for m in range(0,int(max_c) + int(1)):
                if str(n) in lis_r and str(m) in lis_c:
                    try:
                        dic_c[str(m)] = name['name[' + str(n) + '_' + str(m) + ']']
                    except:
                        dic_c[str(m)] = 0
                else:
                    dic_c[str(m)] = 0

            list_all.append(dic_c)

        print(list_all)
        header = ['0','1','2','3','4','5']  # 数据列名

        with open('D:/Documents/Desktop/test.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(list_all)
        f.close()

    return 'nn'


if __name__ == '__main__':
    app.run()