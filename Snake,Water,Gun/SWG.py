# snake Water Gun game 
# Rules 
# 1. snake vs Water : Snanke drinks the water, Snake Wins
# 2. Water vs Gun : Water Wins 
# 3. gun vs snake : gun wins 

# for this game we have to use random choice function, this function generarte random items form the list 

import random 

list = ['s', 'w', 'g']

Chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print('\t\t\tSnake, gun, Water\t\t\t')
# spacify the s,w,g
print('S for Snake\nW for Water\nG for gun')

# creating this game in while loop
while no_of_chance < Chance:
    # this input is for user to choose betwenn snake, water and gun
    _input = input('Snake, Water,Gun: ')
    # and this is a random function, and its generate list items.
    _random = random.choice(list)

    if _input == _random:
        print('Tie, both 0 point to each\n')

# if user choose s, Snake 

# if the user choose snake and computer generate gun then the gun wins and ponint goes to the computer 
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f'You guess {_input} and computer guess {_random} \n')
        print('Computer wins 1 point \n' )
        print(f'Your score is {human_point} and computer score is {computer_point} \n') 

# and in this below statement, if the user choose snake and computer generate the water the the snake wins and point goes to the human 
    elif _input == 's' and _random == 'w':
        human_point = human_point + 1
        print(f'you guess {_input} and computer guess {_random} \n')
        print('you wins 1 point \n')
        print(f'you scare is {human_point} and computer score is {computer_point}')


# if user choose w, water 
    
# if user choose water and comuter generate snake, the computer wins 
    elif _input == 'w' and _random == 's':
         computer_point = computer_point + 1
         print(f'you guess {_input} and computer guess {_random} \n')
         print('computer wins 1 point \n')
         print(f'you scaore is {human_point} and computer score is {computer_point}')

    
# and is user chooser water and computer generate water, the user wins 
    elif _input == 'w' and _random == 'g':
        human_point = human_point + 1
        print(f'you guess {_input} and computer guess {_random} \n')
        print('you win 1 point \n')
        print(f'your score is {human_point} and computer score is {computer_point}')


# if user choose g , gun 

# if user choose gun and computer generate water, water wins 
    elif _input == 'g' and _random == 'w':
        computer_point = computer_point +1
        print(f'you guess {_input} and computer guess {_random} \n')
        print('computer wins 1 point \n')
        print(f'your score is {human_point} and computer score is {computer_point}')

# if user chooser gun and computer generate snake, human wins
    elif _input == 'g' and _random == 's':
        human_point = human_point + 1
        print(f'you guess {_input} and computer guess {_random} \n')
        print('you win 1 point')
        print(f'you score is {human_point} and computer score is {computer_point}')


    else: 
        print('you have wrong input \n')

    no_of_chance = no_of_chance + 1 
    print(f'{Chance - no_of_chance} is left out of {Chance}')

print('Game Over')

# another if/else state for the winner

if computer_point == human_point:
    print('Tie')

elif computer_point < human_point:
    print('you win the match')

else: 
    print('you lost the match and computer wins ')

print(f'you score is {human_point} and comouter score is {computer_point}')