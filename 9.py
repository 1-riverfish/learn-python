# -*- coding: utf-8 -*-

# 关键字参数
def person(name, age, **kw):
    print("name:", name, "age:", age, "others:", kw)

person("wy", 23, kw=None)