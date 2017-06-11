#!/usr/bin/env python3
# _*_ codeing:utf-8 _*_

num = int(input())
# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(num, 'A', 'B', 'C')