# chapter 5 practise set
# 1. write a progaram to create dictionary of hindi and value as their english traslation provifre user with an option to look at it.

dict = {
    'chuuha' : 'mouse',
    'dabba' : 'box',
    'paani' : 'water'
}

print('Your option are: ', dict.keys())
a = input('Enter your Hindi words here ')
# print('English Translation for your hindi words are ' , dict[a])

# below line didn't get an error if we enter a words that is not present.
print('English Translation for your hindi words are ' , dict.get(a))


# 2 write a program to input 8 numbers from the user and display and display all the unique methods
n1 = int(input('Enter a number 1 '))
n2 = int(input('Enter a number 2 '))
n3 = int(input('Enter a number 3 '))
n4 = int(input('Enter a number 4 '))
n5 = int(input('Enter a number 5 '))
n6 = int(input('Enter a number 6 '))
n7 = int(input('Enter a number 7 '))
n8 = int(input('Enter a number 8 '))

uniq = {n1, n2, n3, n4, n5, n6, n7, n8}
print(uniq)

# 3. can we hava a set with 18(int) and 18(str) as a value in it
a = {18, "18"}
print(a)
print(len(a))
print(type(a))
# answer: YES because set can't print repetive values, int(18) and str(18) are both different values that's why we are able to print both 18

# 4. what will be the lenth of the follwing set
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)
print(len(s))
# the lengthof this set is 2 beacuse, int(20) and float(20.0) is same in python that's why set is not including (20.0) and length of this set is 2.

# 5. what is the type of s 
s = {}
print(type(s))
 # the type of s is dictionary <class 'dict'>

# 6. create an empty dictionary and allow 4 friends to enter their fav. lenguare as values and use keys as theri name assume that there name are unique

Dict = {}

a = input('Enter Your Fav. language Tejas')
b = input('Enter Your Fav. language Rishabh')
c = input('Enter Your Fav. language Yash')
d = input('Enter Your Fav. language akshay') 

Dict['Tejas'] = a
Dict['Rishabh'] = b
Dict['Yash'] = c
Dict['akshay'] = d

print(Dict)


# 7. if the name of 2 friends were same what will happen to the program no.6
# Answer: if this happen the lattest value will be printed 
Dic ={}

a = input('Enter Your Fav. language Tejas')
b = input('Enter Your Fav. language Rishabh')
c = input('Enter Your Fav. language Tejas')
d = input('Enter Your Fav. language akshay') 

Dic['Tejas'] = a
Dic['Rishabh'] = b
Dic['Tejas'] = c
Dic['akshay'] = d

print(Dic)

# 8. if the language of 2 friends were same what will happen to the program no.6
myDict = {}

a = input("Enter your Fav language Tejas") 
b = input('Enter your Fav. language Rishabh')
c = input("Enter your Fav. languag Yash")
d = input('Enter your fav. language Akshay')

myDict['Tejas'] = a 
myDict['Rishabh'] = b
myDict['Yash'] = c
myDict['Akshay'] = d

print(myDict) 

# there is no issue if the value of the dictionary is same

# 9. cna you chnage the value inside a list which is containe in set S 
S = {8,7,12,"Lakshay", [1,2]}
print(S)

# this list throw an error because we cannot add a list in a set, and the value of set is not replaceable.

