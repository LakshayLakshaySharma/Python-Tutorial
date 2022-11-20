# # 1. write a program to greet a user with "Good day" using function 

# def greet(name):
#     print("Hello, " + name)

# greet('Lakshay')
   
# # # adding 2 numners 

# def sum(num1, num2):
#     return num1 + num2

# a = sum(10, 20)

# print(a)

# 1. write a pythion program to find the greatest of all tree number 

# for this prgram first me need to get three random number from the user, we can get this numner manually also
# num1 = int(input('Enter numner 1\n'))
# num2 = int(input('Enter numner 2\n'))
# num3 = int(input('Enter numner 3\n'))

# in the findGreatest() function we are comparing all this numner with each other 

# def findGreatest(num1 , num2 , num3):
# # if this if statement we are comparing, if the num1 is greaster than or equals to the num2 and num3, is the num1 is greater then or equals to both num2 and num3 then this function return num1 is the greatest
#     if(num1 >= num2 ) and (num1 >= num3):
#         print(num1)
#     elif(num2 >= num1) and (num2 >= num3):
#         print(num2)

# # if other the statement were false then the num3 is the the largest.
#     else: 
#      print(num3)

# print(findGreatest(56,87,15))
# print(findGreatest(num1 , num2 , num3))


# # 2. write a prgram using function to convert celsus into fahrenheit
# 1 celsius = 33.8 fahrenheit

# # for this function first we can get temperature value in celsius.
# cel = int(input('Enter Temperature in Celsius\n'))

# # then create a function put the formula to convert celcius into fahrenheit 
# def Converter(cel):
#     return (cel*1.8) + 32

# print(Converter(cel))

# # 3 how do you prevent a python print() function to print a new line at the end
# # by using a syntax called end = "", this syntax print your print() function in a array form 

print("lakshay" , end=" ")
print('lakshay sharma')

# # this syntex print lakshay lakshay sharma

# # 4. write a recursion function to calculate the sum of first n natural numner 
# n = int(input('Enter a natural numner\n'))


# def sum(n):
#     if(n == 1 or n == 0):
#         return 1 

#     return n + sum(n-1) 

# print(sum(n))

# # 6. write a python function to convert inches into cm
# #  1 Inch  = 2.54 cm

# Inch = int(input('Enter Your value in Inch\n'))

# def conInch(Inch):
#      return Inch * 2.54

# print(conInch(Inch))

# # 7. write a python function to remove a given word from a list and strip it at a same time




# # 8. write a python function to print the multiplication table of given numner 

# num = int(input('Enter a number\n'))

# def table(num):
#     for i in range(0, 11, 1):
#         print(f"{num} x {i} = {i*num}")

# print(table(num))

