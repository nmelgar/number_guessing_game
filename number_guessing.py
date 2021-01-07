#random number guessing game

import random

#print a randon number
#r = random.randint(1,4)
#print(r)

#this line allows to keep play once you guessed the number
while True:
    flag = True
    while flag:
        num = input('Type a number an upper bound: ')

        #check if the num variable is a number
        if num.isdigit():
            print("Let's Play!")
            num = int(num)
            flag = False

        #this will happen if the user doesn't input a number
        else:
            print('Invalid input! Try Again')

    secret = random.randint(1, num)

    #when the user tries to guess
    guess = None
    #we want the user to know how many tries it took him to guess the right number
    count = 1

    while guess != secret:
        guess = input("Please type a number between 1 and " + str(num) + ":")
        if guess.isdigit():
            guess = int(guess)
        
        if guess == secret:
            print("You got it!")
        else:
            print("Please try again!")
            count += 1

    print("It took you", count, "guesses!")
