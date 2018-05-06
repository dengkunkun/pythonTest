#!/usr/bin/python3
import sys

'''
string = input("\nPlease input your string:")
print(string)
'''

for i in sys.argv:
    print(i)
a,b,c,d = 5,3.4,True,3+3j
print(type(a),type(b),type(c),type(d))
print(isinstance(c,bool))
c = 1
print(isinstance(c,bool))

a = [342,7.3,3+8j,True,'haha,fun']
print(a)
b = ['kidom',888,3.8]
print(a[2:-1])
a[3]='haha'
print(a+b)
