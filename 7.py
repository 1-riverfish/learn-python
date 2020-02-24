# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("bad oprand type")
    s = b**2 - 4*a*c
    if s > 0:
        x1 = (-b + math.sqrt(s)) / (2*a)
        x2 = (-b - math.sqrt(s)) / (2*a)
        return x1, x2
    elif s == 0:
        print("两个相同解.")
        x = -b / (2 * a)
        return x
    else:
        print("无解.")
        return

print("quadratic(2, 3, 1) =", quadratic(2, 3, 1))
print("quadratic(1, 3, -4) =", quadratic(1, 3, -4))

