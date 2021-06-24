import random


barrier = '\n--------------------------------------------------------------'
welcome_message='\n\n\nHello there, and welcome to the random number guessing game!\nThe rules are as follows:\n- There will be three minigames\n- You can choose to guess or create a number for the computer to guess, decide the maximum, and allot the number of guesses'
points_message = '\nThe number of points you receive will depends on how high you cap the maximum, and how many guesses you give.\nIf you\'re guessing, you will receive X / Y points, where X is the maximum number and Y is the number of guesses you were allowed.'
computer_message = ' If the computer is guessing, you will receive X / (X / Y) points if they cannot guess it, and none if they do.\n\n'
print(barrier)
print(welcome_message)
print(points_message)
print(computer_message)
start_game_message = '\nWould you like to guess, or have the the computer guess? Respond with G to guess or C to have the computer guess.'
error_message = 'Error occurred. Please play again.'


games_remaining = 3
points = 0


def game(gr, pts):
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
        user_guess()
    elif game_num == 2:
        cpu_guess()


def cpu_guess():
    return


def user_guess():
    print('\nWhat would you like to guess out of, and how many guesses would you like?\n')
    print('Maximum: \n')
    maximum = input()
    print('Number of guesses: \n')
    guess_num = input()
    number = random.randint(0, maximum)

    for x in guess_num:
        correct_check = False
        print("Guess number " + str(guess_num) + ": \n")
        guess = input()
        correct_check = guess(number, guess)
        if correct_check == True:
            

def guess(num, guess):
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

game(games_remaining, points)
