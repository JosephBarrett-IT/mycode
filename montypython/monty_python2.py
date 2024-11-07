#!/usr/bin/env python3

round = 0
while True:
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    guess = answer.capitalize()
    if guess == 'Brian':
        print('Correct')
        break
    elif guess == 'shrubbery':
        print('You gave the super secret answer!')
        exit()
    elif round == 3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again")
