# chapter 2 practice set
# 1. write a program that add two numbers 

from ast import AnnAssign
from mimetypes import init


a = 20
b = 40
print('the sum of a + b = ' , (a + b))

# 2. write a python program to find remainder when  a numner divided by 2.
a = 2324323
b = 2
print('the remainder of a and b is ' , (a % b))

# 3. check the type of variable assign using input feild.
a = input('the variable type is ' )
print(type(a))

# 4. use comparison operator to find out wheather a given variable a is grater than b or not, a = 34, b = 80
a = 34
b = 80
print(a > b)

#5 . white a python program to find the average of two number enter by the users
a = input('Enter First Numner ')
b = input('Enmter Second Numner ')
a = int(a)    #in input funtion the defaut datatype is string literal, we have to change datatypes manually
b = int(b)
avg = (a + b)/2
print('the average of two number enter by user is ' , avg)

# 6. write a python program to calculate the square root of a number enter by the user
a = input('Enter a numner ')
a = int(a)

print(a * a)