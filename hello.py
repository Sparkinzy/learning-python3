#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

' this is a test module'

__author__ = 'sparkinzy'

import sys
def test():
	args = sys.argv
	if len(args) == 1:
		print('hello ,world')
	elif len(args) == 2:
		print('hello ,%s!' % args[1])
	else:
		print('too many argument')

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
if __name__ == '__main__':
	test()