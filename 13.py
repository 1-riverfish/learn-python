# -*- coding: utf-8 -*-

# 去除字符串首尾的空格

def myTrim(s):
    i = 0
    j = len(s) - 1
    while  i < len(s) and s[i] == ' ':
        i += 1
    while j >= 0 and s[j] == ' ':
        j -= 1
    
    if i > j:
        return ''
    
    return s[i:j+1]

def trim(s):
    while s != '' and s[0] == ' ':
        s = s[1:]
    while s != '' and s[-1] == ' ':
        s = s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')