# chapter -3  practice set

# 1. write a python program to display a user enter name followed by "good afhernoon using input() function "
name = input('Enter your name here  ')
print('Good Afternoon, ' + name)

# 2. write a program to fill in a letter tempelate given below with name and date 
letter = '''dear, <|NAME|>
you are selected
<|DATE|>
'''

name = input('Enter Your Name' ) #input for the name 
date = input('Enter Date')       #input for the date

letter = letter.replace('<|NAME|>', name)   #replacing name and date inthe upper letter string
letter = letter.replace('<|DATE|>', date)
 

print(letter)



# 3. write a program to detect double space in the string
string = "this  is a  a string   with some  double space"
print(string.find("  "))

# 4. replace the doube space from the upper problem with the single space
string = "this  is  a  string  with  double  space"
print(string.replace("  ", " "))

# 5 .write a program to format he following letter using escape character
# letter = "Dear Harry, This python course is noice, Thankyou!"

letter = "Dear Harry,\nthis python course is nice,\nthankyou!"
print(letter)