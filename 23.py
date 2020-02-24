# -*- coding: utf-8 -*-

# 字符串转换成浮点数

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def myStr2float(s):
    left = []
    for i in s:
        if i != '.':
            left.append(i)
        else:
            break
    
    right = s[:len(left):-1]

    def fnL(x, y):
        return x * 10 + y

    def fnR(x, y):
        return x / 10 + y
    
    def char2num(c):
        return DIGITS[c]
    
    # part left .
    leftP = reduce(fnL, map(char2num, left))
    # part right .
    rightP = reduce(fnR, map(char2num, right))

    return leftP + rightP/10

def str2float(s):
    sp = s.split('.')
    se = sp[0] + sp[1]

    def fn(x, y):
        return x * 10 + y

    def char2num(c):
        return DIGITS[c]
    
    return reduce(fn, map(char2num, se)) / 10**len(sp[1])

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
