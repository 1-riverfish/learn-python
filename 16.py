# -*- coding: utf-8 -*-

# 列表生成式

l1 = ['Hello', 'World', 18, 'Apple', None]
l2 = [x.lower() for x in l1 if isinstance(x, str)]

# 测试:
print(l2)
if l2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')