#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# hello world
# 绝对值
a = -100
if a >= 0:
	print(a)
else:
	print(-a)

print('\n')
# 多行不转义
print(r'''\n
这里不是好人
	这里不是好人\t
		你说呢\\
''')
# 多行转义
print('''\n
这里不是好人
	这里不是好人\t
		你说呢\\
''')


# 格式化输出
s1 = 72
s2 = 85
r = (s2-s1) / s1 * 100
print('%.1f%%' % r)

# if
height = 1.75
weight = 80.5
bmi = weight//(height*height)
print(bmi)
if bmi > 32:
	print('严重肥胖')
elif bmi <=32 and bmi > 28:
	print('肥胖')
elif bmi <=28 and bmi > 25:
	print('过重')
elif bmi <=25 and bmi > 18.5:
	print('正常')
else:
	print('偏轻')
