#module used to make a random number
import random
random_num = random.randint(1,10)
previous_guesses = []

inputing = True
while inputing:
    guess = int(input('\nenter num 1-10: '))
    if guess >= 1 and guess <= 10:
        if guess == random_num:
            print('you guessed it')
            previous_guesses.append(guess)
            inputing = False
        elif guess in previous_guesses:
            print('you already guessed ' + str(guess))
            print('choose a different num')
            print('previous guesses: ' + str(previous_guesses))
        else:
            previous_guesses.append(guess)
            if guess > random_num:
                print('random num is lower than ' + str(guess))
            elif guess < random_num:
                print('random num is higher than ' + str(guess))
    else:
        print('enter a valid number')
