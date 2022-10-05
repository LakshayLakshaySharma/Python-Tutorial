# chapter - 6 Conditional Expressrion 

# if/else/elif syntex
# if (condition1):
#     print('yes')
# elif(Condition2):
#     print('no')
# else:
#     print('maybe')

a = 20 
if(a > 10):
    print('A is greater then 10 ')
elif(a < 10):
    print('A is smaller then 10')
else:
    print('a is equals to 10')

print(a)

# if more then one condition were true 
a = 10 
if(10 < 20):
  print('10 is smaller then 20')
elif(10< 30):
    print('10 is smaller then 30')
elif(10<40):
    print('10 is smaller then 40')
else: 
    print('10')
# then the program only print the first true condition.

# multiple if statement 
a = 10 
if (10 < 20):
    print('10 is smaller than 20')

if(10 < 30):
    print('10 is smaller than 30')

if(10 < 40):
    print('10 is smaller than 40')

if(10 > 50):
    print('print than is greater than 50')
else:
    print('10 is not greather then 50')

# logical operators 
# 1. AND OPERATOR
# both condition has to be ture for executing the if statment 
a = int(input('ENter Your Age '))
if(a > 18 and a < 30):
    print('You are young')

else:
    print('you are either a child or and old')

# 2. OR operator 
# either one of the statement should be true for excuting this if statement 
a = int(input("Enter your age "))
if(a > 18 or a == 18 ):
    print('you are an adult')
else:
    print('you are an under age')
