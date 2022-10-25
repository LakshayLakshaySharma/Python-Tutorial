# recurion 

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








