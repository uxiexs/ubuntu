#/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# 把一个序列中的空字符串删掉
#*******************************************************************************

def not_empty(s):
    return s and s.strip()

l1 = input("输入要转换的字符串:")
l2 = str.split(l1,',')
print(list(filter(not_empty,l2)))