import random
import time

barrier = '\n--------------------------------------------------------------'
welcome_message='\nHello there, and welcome to the random number guessing game!\nThe rules are as follows:\n- You choose the number of mini-games you would like to play\n- You can choose to guess or create a number for the computer to guess, decide the maximum, and allot the number of guesses'
points_message = '\nThe number of points you receive will depends on how high you cap the maximum, and how many guesses you give.\nIf you\'re guessing, you will receive X / Y points, where X is the maximum number and Y is the number of guesses you were allowed.'
computer_message = ' If the computer is guessing, you will receive X / (X / Y) points if they cannot guess it, and none if they do.'
print(barrier)
print(welcome_message)
print(points_message)
print(computer_message)
start_game_message = '\nWould you like to guess, or have the the computer guess? Respond with G to guess or C to have the computer guess.'
error_message = 'Error occurred. Please play again.'




def game():
    gr = game_num_ask() # games remaining
    gtotal = gr # so that end number isn't affected
    pts = 0
    for x in range(gr):
        correct_text = False
        game_num = 0 # will be 1 for user guess and 2 for cpu guess
        print('\nYou have '+str(pts)+' points and '+str(gr)+' games remaining!')
        print(start_game_message)
        while correct_text == False:
            sgm_input = input()
            sgm_input= sgm_input.lower()
            if sgm_input == 'g':
                game_num = 1
                correct_text = True
            elif sgm_input == 'c':
                game_num = 2
                correct_text = True
            else:
                print('\nPlease try again. (G to guess, C for the computer to guess.)\n')
        
        if game_num == 1:
            pts += user_guess()
        elif game_num == 2:
            pts += cpu_guess()
        gr -= 1

    print('\nYou finished with '+str(pts) +' points in '+str(gtotal)+' games!')

def cpu_guess():
    print('\nWhat would you like the number to be? ')
    num = int(input())
    maximum = 0
    minimum = 0
    correct = False
    while maximum < num:
        print('\nWhat would you like the maximum to be? (Must be greater than the previous number.) ')
        maximum = int(input())
    print('\nHow many guesses will you allow the computer? ')
    guess_amount = int(input())
    for x in range(guess_amount):
        print('\nThe computer has '+str(guess_amount)+' guesses remaining.')
        guess_val = guess_algorithm(maximum,minimum)
        print('\nThe computer guesses '+str(guess_val)+'!')
        time.sleep(1)
        if num > guess_val:
            print('\nThe number is higher than their guess.')
            maximum = maximum
            minimum = guess_val
        elif num < guess_val:
            print('\nThe number is lower than their guess.')
            maximum = guess_val
            minimum = minimum
        else:
            print('\nCorrect! You lost to the computer.')
            correct = True
            break
        guess_amount -= 1
        time.sleep(2)

    if correct == True:
        return 0
    else:
        return 50

def user_guess():
    print('\nWhat would you like to guess out of, and how many guesses would you like?')
    print('Maximum: ')
    maximum = int(input())
    print('\nNumber of guesses: ')
    guess_num = int(input())
    total_guesses = guess_num # guess number that won't be affected by loop
    number = random.randint(0, maximum)

    correct_check = False
    for x in range(guess_num):
        print('\n'+str(guess_num) + " guesses remaining. Guess here: ")
        guess = int(input())
        correct_check = guess_answer(number, guess)
        guess_num -= 1
        if correct_check == True: 
            break
    if correct_check == False:
        print('Out of guesses!')

    if correct_check == True:
        return maximum / total_guesses
    else:
        return 0

def guess_answer(num, guess):
    if num > guess:
        print('The number is higher than your guess!')
        return False
    elif guess > num: 
        print('The number is lower than your guess!')
        return False
    elif guess == num: 
        print('You got it!')
        return True
    else: 
        print(error_message)
        return False

def game_num_ask():
    print('\nHow many games would you like to play?')
    game_input = int(input())
    return game_input

def guess_algorithm(max,min):
    range = max - min
    guess_val = (range//2) + min
    return guess_val

game()
