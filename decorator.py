#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s: ' % func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def now():
	print('2017-03-01')


# 等同于: now = log(now)
f = now
f()


