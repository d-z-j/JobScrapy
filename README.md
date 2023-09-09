# 实训

## 环境配置

#### 下载软件

1. python
2. PyCharm
3. node.js

#### 创建项目

1. 创建caida文件夹，并用PyCharm打开
2. 创建python虚拟环境。方法有两种：

（1） 在终端输代码：

​	`` python -m venv Infoproject ``

（2）用pycharm快捷创建

3. 创建vue项目，终端输入代码

​	`` vue create my-project``

#### 前端

4. 在vue项目中安装Element-ui

​	`` npm i element-ui -S``

5. 在main.js导入Element-ui

```js
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);

new Vue({
  el: '#app',
  render: h => h(App)
});
```

5. 使用布局容器

```html
<el-container>
  <el-header>Header</el-header>
  <el-container>
    <el-aside width="200px">Aside</el-aside>
    <el-main>Main</el-main>
  </el-container>
</el-container> 
```

6. 并使用他的css样式，在<style>标签中

```css
.el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 5vh;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    height: 95vh;
  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
```

7. 引入NavMenu 导航菜单。在components中创建SideNav.vue

```html
<el-row class="tac">
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>城市</span>
        </template>
        <el-menu-item-group>
          <template slot="title">超一线城市</template>
          <el-menu-item index="1-1">北京</el-menu-item>
          <el-menu-item index="1-2">杭州</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="一线城市">
          <el-menu-item index="1-3">深圳</el-menu-item>
          <el-menu-item index="1-4">上海</el-menu-item>
        </el-menu-item-group>

      </el-submenu>
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">岗位信息</span>
      </el-menu-item>
      <el-menu-item index="4">
        <i class="el-icon-setting"></i>
        <span slot="title">薪资</span>
      </el-menu-item>
    </el-menu>
</el-row>
<script>
  export default {
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>
```

然后再APP.vue中引入创建的组件

```js
<script>
import SideNav from "@/components/SideNav.vue";

export default {
  components:{
    SideNav
}
}
</script>
```

在需要使用组件的地方<SideNav></SideNav>即可使用

8. 在views中创建javatest.vue，关联点击显示内容（router-link和router-view）

javatest.vue

```vue
<template>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="date"
        label="日期"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="地址">
      </el-table-column>
    </el-table>
  </template>

  <script>
    export default {
      data() {
        return {
          tableData: [{
            date: '2016-05-02',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
          }, {
            date: '2016-05-04',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1517 弄'
          }, {
            date: '2016-05-01',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1519 弄'
          }, {
            date: '2016-05-03',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1516 弄'
          }]
        }
      }
    }
  </script>
```

配置router中index.js

先导入javatest.vue

​	`` import javatest from "@/views/javatest.vue"``

在const routes中注册javatest组件

```vue
{
  path: '/javatest',
  name: 'javatest',
  component: javatest
},
```

修改main.js中的内容

```js
import Vue from 'vue'
import App from './App.vue'
import router from './router'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
```

SideNav.vue中的<el-menu-item>标签中添加<router-link>

`` <router-link to="/javatest">北京</router-link>``

App.vue中的<el-main>标签中添加<router-view>

`` <router-view/>``

#### 后端

9. 到虚拟环境目录安装Flask

​	``pip install Flask``

10. 创建后端目录my-server，创建index.py

```python
from flask import Flask,jsonify

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

datas = {
            "date": '2016-05-02',
            "name": '王小虎',
            "address": '上海市普陀区金沙江路 1518 弄'
          }, {
            "date": '2016-05-04',
            "name": '王小虎',
            "address": '上海市普陀区金沙江路 1517 弄'
          }, {
            "date": '2016-05-01',
            "name": '王小虎',
            "address": '上海市普陀区金沙江路 1519 弄'
          }, {
            "date": '2016-05-03',
            "name": '王小虎',
            "address": '上海市普陀区金沙江路 1516 弄'
          }
@app.route("/api")
def api():
    return jsonify(datas)

app.run()
```

11. 联通前后端

javatest.vue中的<script>

```js
export default {

  mounted() {
    fetch("/api").then((res)=>function(){
      return res.json()
    }).then((data)=>function (){
      this.tableData = data
    })
    },
  data() {
    return {
      tableData: []
    }
  }
}
```

vue.config.js中更改跨域

```js
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {
      proxy: {
        "/api": {
          target: 'http://127.0.0.1:5000',
          changeOrigin: true, // 跨域访问设置，true代表跨域
          ws: true,
          'secure': false, // false为http访问，true为https访问
        },
      }
    }

})
```

## 爬虫爬取数据到数据库

12. 创建数据库crawling

字符集utf8mb4

字段：职位名称、地点、学历、工作经验、技术栈、薪资

​	id int 11 key

​	job var 100

​	city var 50

​	education tinyint 

​	workage tinyint

​	skill var 255

​	salary int 11	

13. Scrapy

安装：pip install scrapy

根目录下创建myCrawling：scrapy startproject  myCrawling 

进入myCrawling项目目录： cd myCrawling

创建爬虫程序：scrapy genspider zhaopin zhaopin.com

生成了文件zhaopin.py：

```py
import scrapy


class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['zhaopin.com']
    start_urls = ['https://zhaopin.com/']

    def parse(self, response):
        pass
```

运行这个爬虫程序：scrapy crawl zhaopin

14. 关闭爬虫协议，编写爬取代码

setting.py中注释掉 ``ROBOTSTXT_OBEY = True``这行代码

爬取代码zhaopin.py：

```python
import scrapy
from scrapy import Selector,Request
from myCrawling.items import MycrawlingItem

class ZhaopinSpider(scrapy.Spider):
    name = "zhaopin"
    allowed_domains = ["zhaopin.com"]
    start_urls = ["https://sou.zhaopin.com/?jl=530&kw=java&p=1"]
    def start_requests(self):
        for i in range(1,21):
            yield Request(url=f'https://sou.zhaopin.com/?jl=576&kw=java&p={i}')


    def parse(self, response):
        sel=Selector(response)
        lists=sel.css("#positionList-hook > div > div.joblist-box__item.clearfix")
        for item in lists:
            mydata=MycrawlingItem()
            mydata["job"]=item.css("div.iteminfo__line.iteminfo__line1 > div.iteminfo__line1__jobname > span::attr(title)").extract_first()
            mydata["city"]=item.css("div.iteminfo__line.iteminfo__line2 > div.iteminfo__line2__jobdesc > ul > li:nth-child(1)::text").extract_first()
            mydata["workage"]=item.css("div.iteminfo__line.iteminfo__line2 > div.iteminfo__line2__jobdesc > ul > li:nth-child(2)::text").extract_first()
            mydata["education"]=item.css("div.iteminfo__line.iteminfo__line2 > div.iteminfo__line2__jobdesc > ul > li:nth-child(3)::text").extract_first()
            mydata["skill"]=item.css("div.iteminfo__line.iteminfo__line3 > div.iteminfo__line3__welfare div::text").extract()
            mydata["salary"]=item.css("div.iteminfo__line.iteminfo__line2 > div.iteminfo__line2__jobdesc > p::text").extract_first()

            yield mydata
```

15. 连接数据库，并将爬取数据处理，写入数据库

安装pymysql：pip install pymysql

在pipelines.py配置连接，处理爬取的数据，写入数据库

```py
from itemadapter import ItemAdapter
import pymysql
import re

# Connect to the database
class MycrawlingPipeline:
    def open_spider(self, spider):
        self.connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     database='crawling',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.cursor=self.connection.cursor()
    def close_spider(self, spider):
        self.connection.commit()
        self.connection.close()


    def process_item(self, item, spider):
        # 工作
        item["job"]=re.findall("\w+",item.get("job",""))[0]
        # 城市
        item["city"] = re.findall("\w+", item.get("city"))[0]
        # 工作经验
        result = re.findall("\d+\.{0,1}\d*", item["workage"])
        item["workage"]=(float(result[0])+float(result[1]))/2 if len(result)>0 else 0
        #  学历
        eduType = {"大专": 1, "本科": 2, "硕士": 3, "博士": 4}
        item["education"] = eduType.get(item["education"]) or "其他"
        # 技术
        item["skill"] = ",".join(item["skill"])
        # 薪资
        salaryType = re.findall("(千|万)", item["salary"])
        if (len(salaryType)>0):
            gap = re.findall("\w+\.{0,1}\w*", item["salary"])

            unit1 = float(gap[0].split("千")[0]) * 1000 if len(re.findall("千", gap[0])) > 0 else float(
                gap[0].split("万")[0]) * 10000

            unit2 = float(gap[1].split("千")[0]) * 1000 if len(re.findall("千", gap[1])) > 0 else float(
                gap[1].split("万")[0]) * 10000

            item["salary"] = (unit1 + unit2) / 2
        else:
            item["salary"]=0
        print(item)

        sql = "INSERT INTO `crawling` (`job`, `city`,`workage`,`skill`,`education`,`salary`) VALUES (%s, %s,%s, %s,%s, %s)"
        self.cursor.execute(sql, (
        item["job"], item["city"], item["workage"], item["skill"], item["education"], item["salary"]))
        return item
```

16. 运行爬虫程序

先在setting.py中将下列代码取消注释

```py
ITEM_PIPELINES = {
   'myCrawling.pipelines.MycrawlingPipeline': 300,
}
```

然后在终端，进入myCrawling，运行`` scrapy crawl zhaopin``

运行成功后，在终端查看爬取是否成功，并打开navicat查看是否存入数据库

17. 配置后端读取数据库，返回api接口

index.py文件内容

```py
# 导包
from flask import Flask,jsonify
import pymysql
# 配置连接数据库，取出爬取数据
app = Flask(__name__)
connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     database='crawling',
                                     cursorclass=pymysql.cursors.DictCursor)
cursor=connection.cursor()

sql="select * from crawling"
cursor.execute(sql)
result=cursor.fetchall()
app = Flask(__name__)

# 配置编码格式
app.config['JSON_AS_ASCII'] = False

# 后端接口
@app.route("/api")
def api():
    return jsonify(result)

app.run()
```

运行后端程序，查看是否可以返回json数据

18. 修改前端页面javatest.vue

```vue
<el-table-column
  prop="job"
  label="岗位"
  width="180">
</el-table-column>
<el-table-column
  prop="city"
  label="城市"
  width="180">
</el-table-column>
<el-table-column
  prop="education"
  label="学历">
</el-table-column>
<el-table-column
  prop="workage"
  label="经验">
</el-table-column>
<el-table-column
  prop="skill"
  label="技能">
</el-table-column>
<el-table-column
  prop="salary"
  label="薪酬">
</el-table-column>
```

打开前后端，查看前端页面是否正确显示

## Echarts数据可视化

19. 进入my-project目录，安装Echarts

`` npm install echarts``

20. 在view目录，创建可视化组件java_visible.vue

以下为测试内容

```vue
<template>
<div id="main">

</div>
</template>

<script>
import * as echarts from 'echarts';
export default {
  mounted() {
    var myChart = echarts.init(document.getElementById('main'));
// 绘制图表
myChart.setOption({
  title: {
    text: 'ECharts 入门示例'
  },
  tooltip: {},
  xAxis: {
    data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: [5, 20, 36, 10, 10, 20]
    }
  ]
});
  },
  name: "java_visible"
}
</script>

<style scoped>
#main {
  width: 400px;
  height: 300px;
}
</style>
```

然后在index.js注册组件，必须要在此文件中import

```
{
  path: '/java_visible',
  name: 'java_visible',
  component: java_visible
},
```

然后在SideNav.vue中设置路由到指定位置

`` <router-link to="/java_visible">Java岗位信息可视化</router-link>``

运行看看是否成功，接下来正式开始编写数据可视化页面view_skill.vue

```vue
<template>
 <div id="main">
   数据可视化
 </div>

</template>

<script>
import * as echarts from 'echarts';
 // 基于准备好的 document，初始化echarts实例

export default {
  mounted() {
    var myChart = echarts.init(document.getElementById('main'));
    fetch("/view_skill").then((res)=>{
      return res.json()
    }).then((data)=>{
      // 绘制图表
    myChart.setOption({
      title: {
        text: 'java技能排行榜'
      },
      tooltip: {},
      xAxis: {
        data: data[0]
      },
      yAxis: {},
      series: [
        {
          name: '技能排行',
          type: 'bar',
          data: data[1]
        }
      ]
    });

    })

  },
  name: "view_skill"
}
</script>

<style scoped>
#main{
  width:100%;height:400px;
}
</style>
```

 然后在index.js注册组件，必须要在此文件中import

```js
{
  path: '/view_skill',
  name: 'view_skill',
  component: view_skill
},
```

然后在SideNav.vue中设置路由到指定位置

`` <router-link to="/view_skill">Java岗位信息可视化</router-link>``

在view_skill.vue中的数据需要后端（index.py）从数据库中取出数据并进行处理

```py
@app.route("/view_skill")
def view_skill():
    # 把所有的skill的数据取出来
    cursor = connection.cursor()
    sql = "select skill from crawling"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

    # 1. 先把字典格式转成列表形式
    a=[item.get('skill') for item in result]
    print(a)
    b=[item.split(",") for item in a]
    print(b)
    c=[]
    for item in b:
       c+=item
    print(c)
    result=Counter(c)
    result=result.most_common()[:10]
    skillname=[item[0] for item in result]
    skilldata=[item[1] for item in result]
    return jsonify([skillname,skilldata])
```

如果后端遇到了500，尝试彻底关闭python进程，或者关闭所有端口为5000的进程

如果遇到了404，可以在vue.config.js中配置跨域

```js
devServer: {
    proxy: {
      "/view_skill": {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true, // 跨域访问设置，true代表跨域
        ws: true,
        'secure': false, // false为http访问，true为https访问
      },
```

21. python的爬取、展示、可视化同java的

