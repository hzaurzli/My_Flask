# 纯静态引入vue

利用http-vue-loader.js完成vue子组件的引入

index.html：
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>coding个人笔记</title>
  <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">
</head>
<body>
<div id="app">
  <demo></demo>
  <el-button @click="visible = true">Button</el-button>
  <el-dialog :visible.sync="visible" title="Hello world">
    <p>Try Element</p>
  </el-dialog>
</div>
<script src="https://cdn.bootcdn.net/ajax/libs/vue/2.6.12/vue.min.js"></script>
<script src="https://unpkg.com/http-vue-loader"></script>
<script src="https://unpkg.com/element-ui/lib/index.js"></script>
<script>
  new Vue({
    el: '#app',
    components: {
    // 利用 httpVueLoader 引入 vue 子组件
      'demo': httpVueLoader('./demo.vue')
    },
    data: function() {
      return { visible: false }
    }
  });
</script>
</body>
</html>
```


vue 子组件引入：
```
<template>
    <div class="hello">Hello {{who}}</div>
</template>

<script>
module.exports = {
    data: function() {
        return {
            who: 'world'
        }
    }
}
</script>

<style>
.hello {
    background-color: #ffe;
}
</style>
```

这里需要利用nginx本地化做转发:
nginx下载地址为: [links](http://nginx.org/en/download.html)
![](https://user-images.githubusercontent.com/47686371/202128741-e1e98526-d4a0-4936-bf69-50bc01dca215.png)
下载stable version win版本
![](https://user-images.githubusercontent.com/47686371/202129785-cdeee8d1-4fc6-4e5d-a69e-b809d64eb828.png)
进入conf文件夹，找到nginx.conf文件：
![](https://user-images.githubusercontent.com/47686371/202130791-eb935e9c-59a7-4a6a-9890-e536c714d15e.png)
root 改为待测试html的路径，index 改为待测试的html文件名，注意端口号

双击nginx.exe运行。在浏览器上输入地址：http://localhost:8888/index.html

# 解决flask cor 跨域问题
```
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin # 解决跨域问题

app = Flask(__name__)

app.jinja_env.variable_start_string = '%%'
app.jinja_env.variable_end_string = '%%'

@app.route('/')
@cross_origin()
def pag():
    return render_template("pag.html")


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
```





