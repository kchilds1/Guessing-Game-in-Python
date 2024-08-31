# This is a guess the number game

import random

print('Hello, What is your name')
name = input()
print("Hello, " + name + " I'm thinking of a number between 1 and 20.")
secretNumber = random.randint(1, 20)

for guessessTanken in range(1, 7):
    print("Care to take a guess at what number I'm thinking of?")
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')  
    else:
        break # This condition is for the correct guess

if guess == secretNumber:
    print('Good Job, ' + name + ' You guess my number in ' + str(guessessTanken) + ' guesses')
else:
    print('Nope. Then number I was thinking about was ' + str(secretNumber))

   