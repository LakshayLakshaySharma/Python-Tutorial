# dictionary
myDictionary = {
    "key" : "value",
    "fast" : "very quickly",
    "list" : [1,3,44,5],     #adding a list in a dictionary
    "anotherDictionary" : {"lakshay" : "python"}   #adding a dictionary in a dictionary 
}

# myDictionary["anotherDictionary"] = [324,34,34]
# print(myDictionary["anotherDictionary"])


# methods of dictionary 
# 1. key method  returns the keys of the dictionary 
# print(myDictionary.keys())

# 2. value method return the value of the dictionary 
# print(myDictionary.values())

# 3. items method retutn the whole dictionary in a tuple form
# print(myDictionary.items())

# 4. update dictionary 

# print(myDictionary)
# updatedDict = {
#     "updated keys" : 'updated value',
# }
# myDictionary.update(updatedDict)
# print(myDictionary)

# 5. get method 
print(myDictionary.get('fast'))
# this print function return the same results as the get function, but the major difference between both methods is the the second method return error if the avaliable keys is not available in the dictionary and the first method with get function return none in the key value if not avaliable in the dictionary.
print(myDictionary["fast"])

