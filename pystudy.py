#! /usr/bin/env python
import math
print('Hello Bioinformatics')

r = 3

area = r**2*3.14
print(area)

pi = math.pi
area = r**2*pi
print(area)

num1 = 3
num2 = 5

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)
print(num1%num2)
print(num1//num2)

'''
num = 3 
if num%2 == 0:
    print('짝수')
else:
    print('홀수')

num = 21
if (num%3 == 0) & (num%7 != 0):
    print('3배')
elif (num%7 ==0) & (num%3 !=0):
    print('7배')
else:
    print('3, 7배')

t_sum = 0
for i in range(11):
    t_sum += i
print(t_sum)
'''
for i in range(1,10):
    for j in range(1,10):
        if i%2 == 0:
            print('{}*{}={}'.format(i,j,i*j))
'''
'''
a = 1
total = 1
while a<6:
    total *= a
    a+=1
print(total)

def greet():
    print('Hello, Bioinformatics')

greet()

def greet1() -> None:
    print('Hello, Bioinformatics')

def my_sum(arg1:int,arg2:int) -> int:
    print(arg1+arg2)

my_sum(1,4)
my_sum(2,666)

def my_sum(*arg:int) -> int:
    to_sum = 0
    for i in arg:
        to_sum += i
    return to_sum


print(my_sum(1,4))

inpuuu = input('이름 : ')
print('hello'+' '+inpuuu)
print(inpuuu)
print(type(inpuuu))

inp = input('문자')
if inp.isalpha():
    print('str')
elif inp.isnumeric():
    print('num')

else:
    print('??')


import sys
print(dir(sys))
print(sys.argv)
'''
print(f'run -> pystudy_{sys.argv[1]}.py')

import sys

print(f'hello {ys,argv[1]}')

for i in 1 2 3:
    do
        python sss.py %(i)
    done
        print()
'''
with open('pystudy_1.py','r') as handle:
    for line in handle:
        if line.startswith('>'):
            continue
        print(line.strip)






