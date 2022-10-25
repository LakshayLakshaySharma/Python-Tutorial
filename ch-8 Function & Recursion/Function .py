def percent(marks):
    return  (sum(marks)/400)*100


# percentage with the help of sum function, in pythin sum is a default function to add/sum add the values in the variables
marks = [56,45,77,65]
# per = (sum(marks)/400)*100
per = percent(marks)
print(per)

# # percentage without the help of sum function 

marks2 = [33,56,93,56]
# per2 = ((marks2[0] + marks2[1]+ marks2[2] + marks2[3])/400)*100
per2 = percent(marks2)
print(per2)

def fun():
    print('hello')

# calling this function,
fun()

# default paramenter value 
def greeting(name = "user"):
    print("hello " + name)

greeting()   #return  hello staranger
greeting('lakshay')  # return hello lakshay


# factorial 
# facrotial is a product of all integer numner 
# for eg : factorial of 5 = 5 *4*3*2*1 = 120


n =5 
product = 1
for i in range(n):
    product = product * (i+1)
print(product)

# factorial in function syntex

def factorial(n):
    product = 1 
    for i in range(n):
        product = product * (i+1)
    return product

print(factorial(10))


def factorial_recursive(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial_recursive(n-1)

print(factorial_recursive(6))








