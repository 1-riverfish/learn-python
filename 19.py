# -*- coding: utf-8 -*-

# 高阶函数

def add(a, b, f):
    return f(a) + f(b)

print(add(-1, -2, abs))