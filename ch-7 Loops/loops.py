# loops 
i = 0
while i <5:
    print('greater than 5')
    i = i + 1

# # while loop
fruits = ['apple', 'mango', 'banana', 'grapes', 'kiwi']
i = 0

while i < len(fruits):
    print(fruits[i])
    i = i + 1

# for loop
fruits = ['apple', 'mango', 'banana', 'grapes', 'kiwi']
for items in fruits:
    print(items)


# Range function in for loop
# this funstion help to generate sequence of number
# in this below function the result will the numner between 0-9 the numner 10 will not be included 

for a in range(10):
    print(a)

# starting sequencing number from different numner reader form 0
for a in range(2, 10):
    print(a)


# range function format
# for a in range(start, ends, stepsize):
#       print(a)

# step size in range function 
for a in range(1, 10, 2):
    print(a)

# else statement in for loop
list  = [1,2,3,4]
for items in list:
    print(items)
else:
    print('done')

# break statement 
for a in range(10):
    print(a)
    if(a == 5):
      break

# continue statement 
for i in range(10):
    if(i == 5):
        continue
    print(i)

# Pass Statement 
i = 8
while i > 10:
    pass

if(i == 10):
    pass
print(i)