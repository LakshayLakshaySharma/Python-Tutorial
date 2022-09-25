# chapter 4 practise set
# lists and tuples 

# 1. write a program to store seven fruits in the list enter by the user 

f1 = input('Enter Fruit Number 1 ')
f2 = input('Enter Fruit Number 2 ')
f3 = input('Enter Fruit Number 3 ')
f4 = input('Enter Fruit Number 4 ')
f5 = input('Enter Fruit Number 5 ')
f6 = input('Enter Fruit Number 6 ')
f7 = input('Enter Fruit Number 7 ')

myFruitsList = [f1,f2,f3,f4,f5,f6,f7]
print(myFruitsList)
 
# 2. write a program to accept marks of 6 student and display them in a sort menner
Marks1 = int(input('Enter Your Marks Student 1 : '))
Marks2 = int(input('Enter Your Marks Student 2 : '))
Marks3 = int(input('Enter Your Marks Student 3 : '))
Marks4 = int(input('Enter Your Marks Student 4 : '))
Marks5 = int(input('Enter Your Marks Student 5 : '))
Marks6 = int(input('Enter Your Marks Student 6 : '))

StudentsMarks = [Marks1, Marks2, Marks3, Marks4, Marks5, Marks6]
StudentsMarks.sort()
print(StudentsMarks)

# 3. check that tuple cannot be change in the python 
t = (2,3,13,23,2)
t[1] = 232
print(t)

# 4. write a program to sum a list with 4 number
l = [2,3,4,45]
print(l[0] + l[1] + l[2] + l[3])
print(sum(l)) #this method sum all the list items at once.


# 5. write a program to count the number of 0 in the tuples 
a = (7,0,8,0,0,9)
print(a.count(0))
