#!/usr/bin/python
# -*- coding:utf8 -*-

try:
    print(1/0)
except ZeroDivisionError:
    print("/ by 0")
finally:
    print("finally")
