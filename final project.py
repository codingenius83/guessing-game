#import random module for random numbers
import random

#save a random number as a variable & make list to store you previous guesses
param_x = 1
param_y = 10
number = random.randint(param_x, param_y)

print(number)
attempts = 5
previous_guesses = []

#create a finite loop to count attempts
for i in range(1,attempts + 1):

    #checks if list is empty
    if len(previous_guesses) == 0:
        pass

    #if not empty and you guessed the number u win and the loop breaks
    elif previous_guesses[len(previous_guesses) - 1] == number:
        break

    #variable to break the while loop when needed
    answering = True
    while answering:

        #prints attempts and tries u have left
        print(f'\n--attempt {i}--')

        if i == attempts:
            print(f'you have {6-i} try left')
        else:
            print(f'you have {6-i} tries left')

        #u guess a number
        guess = int(input(f'guess a number ({param_x}-{param_y}): '))

        #makes sure u guess inbetween the numbers
        if guess <= param_y and guess >= param_x:

            #u guessed the right number
            if guess == number:
                print('\nyou guessed the number!!')
                previous_guesses.append(guess)
                answering = False

            #if u already guessed a number and its wrong it ignores it
            elif guess in previous_guesses:
                print('\nyou already guessed ' + str(guess))
                print('choose a different num')
                print('previous guesses: ' + str(previous_guesses))

            else:

                #if this is ur final attempt and u got it wrong game over
                if i == attempts:
                    previous_guesses.append(guess)
                    print('\nyou ran out of tries')
                    print(f'your guesses were:\n{previous_guesses}')
                    print(f'the correct number was {number}')
                    print('gave over! xd')

                #tells u that u guessed too high
                if guess > number:
                    previous_guesses.append(guess)
                    print(f'\nrandom number is lower than {str(guess)}')
                    answering = False

                #tells u that u guessed too low
                elif guess < number:
                    previous_guesses.append(guess)
                    print(f'\nrandom number is higher than {str(guess)}')
                    answering = False

        #if not between params then it doest count it
        else:
            print('enter a valid number')

        
    