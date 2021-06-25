import random # for random number generation
import time # for slowing down the computer guessing

# start messages
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

# doesn't take or return any variables
def game(): # main game runner
    gr = game_num_ask() # games remaining
    gtotal = gr # so that end number isn't affected
    pts = 0
    for x in range(gr):
        correct_text = False # correct meaning the user inputted a valid answer (either 'g' or 'c')
        game_num = 0 # will be 1 for user guess and 2 for cpu guess
        print('\nYou have '+str(pts)+' points and '+str(gr)+' games remaining!')
        print(start_game_message)
        while correct_text == False:
            sgm_input = input() # input from "Respond with G to guess or C to have the computer guess"
            sgm_input= sgm_input.lower()
            if sgm_input == 'g': # meaning the user would like to guess
                game_num = 1
                correct_text = True
            elif sgm_input == 'c': # meaning the user wants the computer to guess
                game_num = 2
                correct_text = True
            else: # meaning the user inputted an invalid answer
                print('\nPlease try again. (G to guess, C for the computer to guess.)\n')
        
        if game_num == 1:
            pts += user_guess() # invokes user guessing mini-game and adds the points they receive to their total
        elif game_num == 2:
            pts += cpu_guess() # invokes computer guessing mini-game and adds the points they receive to their total
        gr -= 1

    print('\nYou finished with '+str(pts) +' points in '+str(gtotal)+' games!\n')

# no pre-condition
# returns an int representing the number of points the player earned from the mini-game
def cpu_guess(): # computer guessing mini-game
    print('\nWhat would you like the number to be? ')
    num = int(input()) # user-inputted number choice
    maximum = 0
    minimum = 0 # not inputted by user, used by computer to guess
    correct = False # bool for if the computer correctly guessed
    while maximum < num: # repeats until the user enters a valid maximum
        print('\nWhat would you like the maximum to be? (Must be greater than the previous number.) ')
        maximum = int(input()) # user-inputted maximum
    print('\nHow many guesses will you allow the computer? ')
    guess_amount = int(input()) # user-inputted number of guesses
    for x in range(guess_amount): # loops until cpu is out of guesses or has guessed it
        print('\nThe computer has '+str(guess_amount)+' guesses remaining.')
        guess_val = guess_algorithm(maximum,minimum) # calls cpu guessing algorithm and takes the return int as the guess
        print('\nThe computer guesses '+str(guess_val)+'!')
        time.sleep(1) # so that the computer's response feels more humanlike
        if num > guess_val: # if the computer guesses low
            print('\nThe number is higher than their guess.')
            maximum = maximum # keeps the maximum
            minimum = guess_val # raises minimum to cpu guess so they don't guess lower than they should
        elif num < guess_val: # if the computer guesses high
            print('\nThe number is lower than their guess.')
            maximum = guess_val # lowers maximum to guess value so that the computer doesn't guess higher than they should
            minimum = minimum # keeps the minimum
        else: # if the computer's guess matches the number
            print('\nCorrect! You lost to the computer.')
            correct = True
            break # break out of loop
        guess_amount -= 1 # so that it doesn't print that the computer is taking the same guess again
        time.sleep(2) # so that the computer's response feels more humanlike

    if correct == True: # if the cpu guesses correctly don't give user points
        return 0
    else: # if the computer doesn't guess give points to user
        return 50

def user_guess():
    print('\nWhat would you like to guess out of, and how many guesses would you like?')
    print('Maximum: ')
    maximum = int(input()) # takes user input for maximum
    print('\nNumber of guesses: ')
    guess_num = int(input()) # takes user input for number of guesses allowed
    total_guesses = guess_num # guess number that won't be affected by loop
    number = random.randint(0, maximum) # uses 'random' library to generate a random number for the user to guess

    correct_check = False # flag for if the user guesses correctly
    for x in range(guess_num):
        print('\n'+str(guess_num) + " guesses remaining. Guess here: ")
        guess = int(input()) # takes user input as their guess
        correct_check = guess_answer(number, guess) # bool value for whether their guess is correct or not
        guess_num -= 1 # so that it doesn't print that the user is taking the same guess again
        if correct_check == True: 
            break # breaks out of loop if user guessed correctly
    
    if correct_check == False: # if when the loop ends the user still hasn't gotten it
        print('Out of guesses!')

    if correct_check == True: # gives user points if they guess correctly
        return maximum / total_guesses
    else: # no points if they don't guess correctly
        return 0

# takes the number and number guessed as input
# returns a boolean value whether or not they match, and prints a message
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

# doesn't take any variables
# returns the number of mini-games the user wishes to play
def game_num_ask():
    print('\nHow many games would you like to play?')
    game_input = int(input())
    return game_input

# takes maximum and minimum ints as input
# returns the computer's guess as an int
def guess_algorithm(max,min):
    range = max - min
    guess_val = (range//2) + min
    return guess_val

# runs the game
game()
