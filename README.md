# flask-movie
使用flask的一个练手电影网站

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

