# -*- coding: utf-8 -*-

# log("execute") and log()

import functools

def log(param):
    if isinstance(param, str):
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print(param)
                return fn(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(param)
        def wrapper(*args, **kw):
            return param(*args, **kw)
        return wrapper

@log("Test")
def testA():
    print("test A")


@log
def testB():
    print("test B")

testA()
testB()