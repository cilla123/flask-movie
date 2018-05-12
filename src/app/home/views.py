# -*- coding:utf-8 -*-
__author__ = 'Ben'

from . import home

@home.route("/")
def index():
    return "123123"