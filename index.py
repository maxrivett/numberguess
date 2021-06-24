barrier = '\n--------------------------------------------------------------'
welcome_message='\n\n\nHello there, and welcome to the random number guessing game!\nThe rules are as follows:\n- There will be three minigames\n- You can choose to guess or create a number for the computer to guess, decide the maximum, and allot the number of guesses'
points_message = '\nThe number of points you receive will depends on how high you cap the maximum, and how many guesses you give.\nIf you\'re guessing, you will receive X / Y points, where X is the maximum number and Y is the number of guesses you were allowed.'
computer_message = ' If the computer is guessing, you will receive X / (X / Y) points if they cannot guess it, and none if they do.\n\n'
print(barrier)
print(welcome_message)
print(points_message)
print(computer_message)
start_game_message = '\nWould you like to guess, or have the the computer guess? Respond with G to guess or C to have the computer guess.'

games_remaining = 3
points = 0


def game(gr, pts):
    correct_text = False
    print('\nYou have '+str(pts)+' points and '+str(gr)+' games remaining!')
    print(start_game_message)
    while correct_text == False:
        sgm_input = input()
        sgm_input= sgm_input.lower()
        if sgm_input == 'g':
            user_guess()
            correct_text = True
        elif sgm_input == 'c':
            cpu_guess()
            correct_text = True
        else:
            print('\nPlease try again. (G to guess, C for the computer to guess.)\n')


def cpu_guess():
    return


def user_guess():
    return

game(games_remaining, points)
