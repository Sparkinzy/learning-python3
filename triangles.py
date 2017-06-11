#!/usr/bin/env python3
# _*_ codeing:utf-8 _*_
# 杨辉三角

# def triangles():
# 	n,level_upper =1,[]
# 	while True:
# 		if n == 1:
# 			level = [1]
# 			level_upper = level
# 		else:
# 			level = []
# 			level.append(1)
# 			for k in range(1,len(level_upper)):
# 				level.append(level_upper[k-1]+level_upper[k])
# 			level.append(1)
# 			level_upper = level;

# 		n = n+1
# 		yield level

def triangles():
	L = [1]
	while True:
		yield L
		L = [1] + [L[x-1]+L[x] for x in range(1,len(L))] +[1]

n = 0
for t in triangles():
	print(t)
	n = n+1
	if n == 10:
		break