# -*- coding: utf-8 -*-

# 生成器-杨辉三角形

def myTriangles():
    previous = []

    i = 1
    while True:
        present = []

        for j in range(0, i):
            if j == 0 or j == i-1:
                present.append(1)
            else:
                present.append(previous[j-1] + previous[j])
        
        yield present
        previous = present
        i += 1
    

# 标准答案
def triangles():
    l = [1]
    while True:
        yield l
        l = [1] + [l[i] + l[i+1] for i in range(0, len(l)-1)] + [1]
    
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')