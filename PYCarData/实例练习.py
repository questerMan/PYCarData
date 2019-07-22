#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:47:01 2019

@author: lixin
"""

#导入复数数学模块
import cmath as ca

#1、输出实例

#print('Hello word!')

'''
#2、输入计算两个数的和

num1 = input("请输入第一个数： ")
num2 = input("请输入第二个数： ")

num_sum = int(num1) + int(num2)

print("计算结果：{}".format(num_sum))
'''
'''
#3、计算一个数的平方根
num = input("请输入一个数字： ")
num_sqrt = ca.sqrt(int(num))
print(num_sqrt)
'''
'''
#4、计算二次方程

# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0

a = float(input("请输入a的值（不为0）："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))

#计算方程
d = b**2-4*a*c

#两种求解方式
sol1 = (-b-ca.sqrt(d))/(2*a)
sol2 = (-b+ca.sqrt(d))/(2*a)

print("一元二次方程的解是：x1={:.2f},x2={:.2f}".format(sol1,sol2))
'''
'''
#5、计算三角形的周长和面积

#输入已知三角形的三条边
a = float(input("请输入三角形第一条边长度："))
b = float(input("请输入三角形第二条边长度："))
c = float(input("请输入三角形第三条边长度："))

#计算周长
h = a+b+c

#计算面积
s = (h/2*(h/2-a)*(h/2-b)*(h/2-c)) ** 0.5

print("三角形的周长是{},面积是{:.0f}".format(h,s))
'''

'''
#6、九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print("{}x{}={} ".format(j,i,i*j),end = '')
    print()
'''
'''
#7、线性查找
def search(arr,n,x):
    for i in range(n):
        if arr[i]==x:
            return i
        print("--{}--".format(i))
    return -1

arr = ['A','B','C','D','E','F']
n = len(arr)
x = 'E'
result = search(arr,n,x)
if result == -1:
    print('元素不在列表中')
else:
    print('元素在数组中的索引为：{}'.format(result))

'''
