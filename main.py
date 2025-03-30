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

#3rd
import math as m
q = 3
while m.sqrt(q) - round(m.sqrt(q)) != 0:
    q = int(input('enter number'))
    if m.sqrt(q) - round(m.sqrt(q)) != 0:
        print('full sqrt')
        break

#4th
num = int(input('enter integer number -->'))
print(sum(range(1, num+1)))

#5th
from numpy.ma.core import floor

val_in = int(input())
val_max = int(floor(val_in ** (1/3)))
for i in range(1, val_max+1):
    print(i**3, end=' ')

#6th
subscribes = int(input())
k = 1
while subscribes > k:
    print(k)
    k*=2

#7th
answer = int(input())
k = 1
while answer > k:
    k *= 2
if k == answer:
    print('верно')
else:
    print('неверно')

#8th
xmmm = int(input())
k = 1
while 2**k <= xmmm:
    k += 1
print(k)

#9th
lst = list(map(int, input().split()))
prot = 1 + (lst[1]/100)
days = 1
while lst[2] > lst[0]:
    lst[0] *= prot
    days +=1
print(days)

#10th
temp = []
lower = 0
while int(input()) != 0:
    temp.append(float(input()))
for i in range(1, len(temp)):
    if temp[i] > temp[i+1]:
        lower += 1
print(lower)