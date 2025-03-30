'''
#1st
num = []
dels = 0
for i in range(1, 101):
    num.append(i)
for k in range(0, 100):
    if num[k]%17 == 0:
        dels +=1
print(dels)


#2nd
strr = input()
strn = []
for i in range(0, len(strr)):
    if i % 3 == 2:
        strn.append(strr[i])
print(strn)

import math as m
q = 3
while m.sqrt(q) - round(m.sqrt(q)) != 0:
    q = int(input('enter number'))
    if m.sqrt(q) - round(m.sqrt(q)) != 0:
        print('full sqrt')
        break

num = int(input('enter integer number -->'))
print(sum(range(1, num+1)))

from numpy.ma.core import floor

val_in = int(input())
val_max = int(floor(val_in ** (1/3)))
for i in range(1, val_max+1):
    print(i**3, end=' ')
'''


