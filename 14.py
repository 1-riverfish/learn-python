# -*- coding: utf-8 -*-

# 查找一个列表中的最大值和最小值，并以元组的形式返回

def findMinAndMax(l):
    if len(l) == 0:
        return None, None
    min = l[0]
    max = l[0]
    for i in l:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')