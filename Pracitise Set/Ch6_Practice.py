# 1. write a program to print yes when the age entered by the user us greater than or equal to 18
# using int in input because the default datatype in input is str and age sould be in integer and using locial operator in str show erre
a = int(input('Enter Your Age : '))
if(a >= 18):
     print('your age is greater than or equals to 18 you can enter this program')
else:
    print('Your age should be greater than 18 for entering this program')

# 1. write a program to find greatest of four numbers enterd by the useres 

num1 = int(input('Enter number1 '))
num2 = int(input('Enter number2 '))
num3 = int(input('Enter number3 '))
num4 = int(input('Enter number4 '))

# in this below code we compare num1 to num4, if num1 is greater then f1 = num1 otherwise f1=num4 and we will check this for the num2 and num3
if(num1 > num4):
     f1 = num1
else: 
     f1 = num4


if(num2 > num3):
   f2 = num2
else:
     f2 = num3

if(f1>f2):
     print(f1 , 'is the greatest number of all')
else: 
     print(f2, 'is the greatest number of all')


# 2. write a program to find out wheather a student is pass or fail if it required total 40% and atleast 33% in each subject to pass assume 3 subject and take marks as an input form the user 

sub1 = int(input("Enter your first subject's marks\n "))
sub2 = int(input("Enter your first subject's marks\n "))
sub3 = int(input("Enter your first subject's marks\n "))

# in this line of code we are checking that if all the subject's marks is less than 33 
if(sub1< 33 or sub2< 33 or sub2<33):
     print('You are failed in this exam')
# in this code we are checking is that total percentage is less than 40%
elif(sub1 + sub2+ sub3)/3 < 40:
     print('you are failed because you score is less than 40%')
else:
     print('pass')


# 3. a span massage is defined as a text containg following keywords: 
# 'make a lot of money' , "buy now", "subscribe this", "click this", write a program to detect these

text = input('')

# # in this if/else statement we are checking if this text is in the user's text not, if this text is in the user's text spam = true other keep it false.
if('make a lot of money' in text):
     spam = True
elif('but now' in text):
     spam = True
elif('subscribe this' in text):
     spam = True
elif('click this' in text):
     spam = True
else:
     spam = False

# # if the spam is true then print this text
if(spam):
     print('this text is a spam')
else:
     print('this text is not a spam')

# 4. write a program to find wheather a given username contains less than 10 character or not
name = input('Enter Your Name here\n')

if(len(name) > 10):
     print('this name contains charcter more than 10')
else:
     print('this name containes character less than 10')
     
# 5. write a program to find out wheather given name is present is a list or not
namel = ['lakshay', 'tejas', 'rishabh', 'yash']

if('lakshay' in namel):
     print ('yess this name is in a list')
else:
     print('no this name is not present is a list')

# 6. write a program to calulate the grades of a student from this marks from the following student 
marks = int(input("Enter Your Marks : "))
 
if(marks < 100 and marks > 90):
     print('Excelent')
elif(marks < 90 and marks > 80):
     print('A Grade')
elif(marks < 80 and marks > 70):
     print("B Grade")
elif(marks < 70 and marks > 60):
     print("C Grades")
elif(marks < 60 and marks > 50):
     print('D Grades')
elif(marks < 50):
     print('Fail')

# 7. write a program to find out wheather a given post is talking about lakshay or not
post = input('Write a post Below\n')
if('lakshay' in post):
     print('lakshay is in the post')
else:
     print('lakshay is not is a post')


