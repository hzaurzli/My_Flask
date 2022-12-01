# 纯静态引入树文件
利用http-vue-loader.js画进化树

index.html：
```
<!DOCTYPE html>
<html lang='en'>

<head>
  <meta charset="utf-8">

  <link rel="stylesheet" type="text/css" href="http://yanglab.hzau.edu.cn/static/resource_js/exp/phylotree.css">
<link rel="stylesheet" type="text/css" href="http://yanglab.hzau.edu.cn/static/css/bootstrap.min.css">
<script type="text/javascript" charset="utf8" src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
<script type="text/javascript" charset="utf8" src="http://yanglab.hzau.edu.cn/static/resource_js/exp/d3.v3.min.js"></script>
<script type="text/javascript" charset="utf8" src="http://yanglab.hzau.edu.cn/static/js/underscore-min.js"></script>
<script type="text/javascript" charset="utf8" src="http://yanglab.hzau.edu.cn/static/resource_js/exp/phylotree.js"></script>
</head>

<body>
 <div>
  <svg id="tree_display" style="width:320px"></svg>
</div>

<script>
  $(document).ready(function() {
    var file_name = './tree.nwk'; //加载nwk进化树文件，自行修改文件路径
    d3.text(file_name, function(error, newick) {
      var height = 550,
        width = 290,
        tree = d3.layout.phylotree()
          .svg(d3.select("#tree_display"))
          .options({
            'left-right-spacing': 'fit-to-step',
            'top-bottom-spacing': 'fit-to-size',
            'selectable': true,
            'reroot': false,
            'hide': false,
            'show-scale': false
          })
          .align_tips(true)
          .font_size(14)
          .size([height, width])
          .node_circle_size(0);
      tree(newick).layout();
      function my_node_style_text(node) {
        node['text-italic'] = !node['text-italic'];
        d3.layout.phylotree.trigger_refresh(tree);
      }
      function my_menu_title(node) {
        if (node['text-italic']) {
          return "Remove Italics";
        }
        return "Custom function";
      }
      tree.get_nodes()
        .filter(d3.layout.phylotree.is_leafnode)
        .forEach(function(tree_node) {
          d3.layout.phylotree.add_custom_menu(tree_node, // add to this node
            my_menu_title, // display this text for the menu
            function() { //Custom function
              console.log(tree_node['name'])
            },
            d3.layout.phylotree.is_leafnode
          );
        });
    })
  })
</script>
</body>

</html>
```

![](https://user-images.githubusercontent.com/47686371/204993911-0a1c6d12-dded-421e-832b-bc035a6c5a79.png)
进入conf文件夹，找到nginx.conf文件,修改路径

双击nginx.exe运行。在浏览器上输入地址：http://localhost:8888/index.html
![](https://user-images.githubusercontent.com/47686371/204994471-54e95d64-96ca-4667-bc5a-9fd71e9f7020.png)

