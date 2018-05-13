# flask-movie
使用flask的一个练手电影网站

## 运行

- 1.打开pycharm，在preferences搜索Project Interpreter选择虚拟环境flask-movie下的venv，然后点击ok
- 2.然后选择flask-movie中的manage.py，右击run manage

注意，一定要有根据数据库来配置，这里不会用的话，直接用数据库默认配置

本项目的数据库

- 数据库名：flask_movie
- 用户名：root
- 密码：root
- host: 127.0.0.1
- password: root
- prot: 3306

mysql+pymysql://root:root@127.0.0.1:3306/flask_movie

## 一、virtualenv的使用

- 1.创建虚拟环境：virtualenv venv
- 2.激活虚拟环境：source venv/bin/activate
- 3.退出虚拟环境：deactivate

## 二、flask的安装

- 1.安装前检测：pip freeze
- 2.安装flask：pip install flask
- 3.安装后检测：pip freeze

期间可能需要翻墙，所以指定源：

```python
pip3 install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com flask
```

## 三、前后台项目目录分析

项目有三个：

前台模块

后台模块

小程序模块


### 蓝图构建项目目录

- 1.定义蓝图(app/admin/__init__.py)

```python
from flask import Blueprint
admin = Blueprint("admin", __name__)
import views
```

- 2.注册蓝图(app/__init__.py)

```python
from admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix="/admin")
```

- 3.调用蓝图(app/admin/views.py)

```python
from . import admin
@admin.route("/")
```

## 四、会员及会员登录日志数据模型设计

### 1.安装数据库连接依赖包

ORM:([flask-sqlalchemy学习](http://www.pythondoc.com/flask-sqlalchemy/config.html))

```python
pip install flask-sqlalchemy
```

### 2.定义mysql数据库连接

```python
from flask-sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost/movive"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
```




























