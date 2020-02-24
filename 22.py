# -*- coding: utf-8 -*-

# 接受一个list并求积

from functools import reduce

def prod(l):
    def fn(a, b):
            return a * b
    
    return reduce(fn, l)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    
