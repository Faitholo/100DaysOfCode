#!/usr/bin/python3

# This will request for user input
# Inputs will be used to check if
# The user guesses ghe right number.


# Ask for user input
guess = (input('Would you like to guess our lucky number? Yes or No :'))

if guess == 'Yes':
    input('Great! Now, try to guess a number between 1 and 10: ')
    if input == 3:
        print('Correct! You guessed the number right!')
    else:
        print('Sorry, better luck next time!')
        
else:
    print('Okay Bye!')
    