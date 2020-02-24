# -*- coding: utf-8 -*-

l = [1, 2, 3]
x = 1
t = (l, x)
# t[1] = 2 TypeError: 'tuple' object does not support item assignment
t[0][0] = 2
print("t:", t)