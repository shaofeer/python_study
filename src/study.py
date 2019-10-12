#!/usr/bin/python
# -*- coding:utf-8 -*-

# with open("wc.txt") as file:
#     for line in file:
#         print(line.rstrip())
#
# with open("newfile.txt",mode='w') as f:
#     f.write("I am new File\r\n")
#     f.write("I am new File\r\n")
#     f.write("I am new File\r\n")
#     f.write("I am new File\r\n")

name = input("input your name:")
with open('guest.txt', mode='a') as namef:
    namef.write(name + "\n")

print("welcome!" + name)
