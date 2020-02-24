# -*- coding: utf-8 -*-

# 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字

def normalize(name):
    def clower(c):
        return c.lower()
    
    s = name[0].upper()
    for ch in map(clower, name[1:]):
        s += ch

    return s

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


