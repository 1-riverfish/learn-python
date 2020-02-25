# -*- coding: utf-8 -*-

# 计算素数 埃氏筛法

def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisiable(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisiable(n), it)

# 生成1000以内素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

