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

