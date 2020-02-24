# -*- coding: utf-8 -*-

# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

# person("wy", 23) TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'
person("wy", 23, city="lyg", job="student")