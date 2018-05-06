#!/usr/bin/python
import re
import math
import cmath
import random

a=3
b=8.3
del a
print b
print hex(int(b))

a=[3,8.4,4+3j,3432L]
b=(8,9.3,'haha')
c={1:'banana',2:'appale',3:'mango'}
print a,b,c
if 3 in a:
    print '3 in a'
else:
    print 'a is not in a'

if 3 not in b:
    print '3 is not in b'
else:
    print '3 is in b'


print r'\nhaha'

d=['Hello']
d.append(' Runoob')
print d

class Vector:
    classAttr=0

    def __init__(self,a):
        self.a=a
        classAttr=a

    def __add__(self,other):
        return self.a+other.a

    def __str__(self):
        return "Vector:%d"%self.a

v1=Vector(3)
v2=Vector(5)
print v1+v2
       
string = '38409705384'

string = re.sub(r'8',' ',string)
print string 

s='a767bc645jdljfabc565466dlfjlabc445jf23ldj342aab342c'
m=re.search('\d',s)
print m.group(0)
print m.groups()



