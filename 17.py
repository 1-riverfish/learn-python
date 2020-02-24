# -*- coding: utf-8 -*-

# 斐波那契数列生成器

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
        
    return("Done")

fibGen = fib(6)

for i in fibGen:
    print(i)
