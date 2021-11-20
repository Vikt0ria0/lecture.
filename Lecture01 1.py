import math
print('ведите значение длины сторон')
print ('a=')
a=int(input())
if a>0:
    print ('False')
print ('b=')
b=int(input())
if b>0:
    print ('False')
print ('d=')
d=int(input())
if d>0:
    print ('False')
print(math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(d))))
