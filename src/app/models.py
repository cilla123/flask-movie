# -*- coding:utf-8 -*-
__author__ = 'Ben'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/flask_movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

# 会员
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    avatar = db.Column(db.String(255), unique=True)
    uuid = db.Column(db.String(255), unique=True)
    create_time = db.Column(db.DateTime, index=True, default=datetime.utc)
    update_time = db.Column(db.DateTime, index=True, default=datetime.utc)

    def __repr__(self):
        return "<User %r>" % self.name

# 会员登录日志
class Userlog(db.Model):
    __tablename__ = "user_log"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    ip = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, index=True, default=datetime.utc)
    update_time = db.Column(db.DateTime, index=True, default=datetime.utc)

    def __repr__(self):
        return "<Userlog %r>" % self.id

# 标签
class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    create_time = db.Column(db.DateTime, index=True, default=datetime.utc)
    update_time = db.Column(db.DateTime, index=True, default=datetime.utc)

    def __repr__(self):
        return "<Tag %r>" % self.name








