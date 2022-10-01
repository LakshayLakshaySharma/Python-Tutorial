# sets
a = {1,2,3,4,5,6,1}
print(a)   # returns {1, 2, 3, 4, 5, 6}
print(type(a))  #return  <class 'set'>

# empty sets
b = {}
print(b)
print(type(b)) #return <class 'dict'>

c = set()
c.add(3)
c.add(4)
c.add(5)
print(c) 
print(type(c))  #return #return <class 'set'>


# set methods 
# 1. len method
s = {1,2,4,5}
print(len(s))

# 2. remove method
s = {1,2,4,5}
s.remove(2)
print(s)

# 3. pop methods
s = {1,2,4,5}
print(s.pop())
print(s)

# 4. clear
s = {1,2,4,5}
s.clear()
print(s)