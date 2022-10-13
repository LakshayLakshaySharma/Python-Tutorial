# # 1. write a program to print 1 to 50 using a while loop
a = 1
while a < 51:
    print(a)
    a = a + 1

# # 2. print "lakshay" 5 times
b = 0
while b < 5:
    print('lakshay')
    b = b + 1

# 3. wriet a program to print content of a list using while loop
fruits = ['apple', 'mango', 'banana', 'grapes', 'kiwi']
i = 0

while i < len(fruits):
    print(fruits[i])
    i = i + 1

# in this condition, while the length is fruits is less than i print fruits[i]

# 4. write a program to print multiplication table of a given number using for loop and while loop both
# for this program first we need a number that we are going to ask with a user
num = int(input('Enter A Numner\n'))

# .for loop
for i in range(1, 11):
    # print( str(num) + "x" + str(i) + "=" + str(i*num) )
    # f-string
    print(f"{num} x {i} = {i*num}")

# 5. write a program to greet all the person stored in a list li and which starts with S
# for this program we had to use .startwith method

list = ['Lakshay', "Lala", "tejas"]
for i in list:
    if(i.startswith('L')):
        print('Hello ' + i)



# 6.write a program to check weater a given numner is prime or not
# for this progrm first we need a numner from user
num = int(input('Enter a numner\n'))
prime = False

# # in this for loop we are checking weather the reminder is 0 or not, for checking the reminder we use percent sign(%)
for i in range(2, num):
    if(num%i == 0):
        prime = True
# we are breaking this loop because we use this loop for once
        break

if(prime):
    print('Prime Number')
else:
    print('Not a Prime Number')

# 7 write a program to find the sum of first n natural number using while loop 
n = int(input('Enter a number'))
i = 0
while i < n:
    i = i+1
    print(i)

# 8. write a program to calculate the factorial of a given number using for loop 
# factorial of 5 is 1 x 2 x 3x 4x 5x 

num = int(input('Enter a Numner\n'))
fac = 1

for i in range(1 , num+1):
    fac = fac * i
    print(f"the Factorial of {num} is {fac}")


# 9.write a program to print the following start pattern 
#       *
#      ***
#     *****

n = 3
for i in range(3):
    print(" " * (n-i-1), end="") #for eliminate the extra one line space after print function  
    print("x" * (2*i+1), end="")
    print(' ' * (n-i-1))

# 10. write a program to print the following start pattern 
# *
# **
# ***

n = 4
for i in range(4):
    print('x' * i)

# 11. write a program to print the following start pattern
#  * * *
#  *   *
#  * * *
# 
n = 3
for i in  range(3):
  print('x' * 3)

# 12. write  a prgram to print multiplication table of n using for loop in reversed order
num = int(input('Enter a number'))

for i in range(10 , 0 , -1):
    print(f"{i} x {num} = {i*num} ")