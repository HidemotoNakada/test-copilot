# Rock-paper-sissors game
# import random module
import random

# define main function
def main():
    # define variables
    # set accumulator to 0
    wins = 0
    losses = 0
    ties = 0
    # set sentinel to 'y'
    again = 'y'
    # set loop to continue while again is 'y'
    while again == 'y':
        # call get_comp_choice function and assign to variable
        comp_choice = get_comp_choice()
        # call get_user_choice function and assign to variable
        user_choice = get_user_choice()
        # call determine_winner function and assign to variable
        winner = determine_winner(comp_choice, user_choice)
        # call display_winner function and pass winner variable
        display_winner(winner)
        # call display_score function and pass winner variable
        wins, losses, ties = display_score(winner, wins, losses, ties)
        # call play_again function and assign to again variable
        again = play_again()

# define get_comp_choice function
# no parameters
# return comp_choice
# 
# generate random number between 1 and 3
# if number is 1, set comp_choice to 'rock'
# else if number is 2, set comp_choice to 'paper'
# else set comp_choice to 'scissors'
# return comp_choice
def get_comp_choice():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = 'rock'
    elif comp_choice == 2:
        comp_choice = 'paper'
    else:
        comp_choice = 'scissors'
    return comp_choice

def display_winner(winner):
    print('The winner is', winner)
def display_score(winner, wins, losses, ties):
    if winner == 'user':
        wins += 1
    elif winner == 'computer':
        losses += 1
    else:
        ties += 1
    print('Wins:', wins, 'Losses:', losses, 'Ties:', ties)
    return wins, losses, ties

def determine_winner(comp_choice, user_choice):
    if comp_choice == user_choice:
        winner = 'tie'
    elif comp_choice == 'rock' and user_choice == 'paper':
        winner = 'user'
    elif comp_choice == 'rock' and user_choice == 'scissors':
        winner = 'computer'
    elif comp_choice == 'paper' and user_choice == 'rock':
        winner = 'computer'
    elif comp_choice == 'paper' and user_choice == 'scissors':
        winner = 'user'
    elif comp_choice == 'scissors' and user_choice == 'rock':
        winner = 'user'
    elif comp_choice == 'scissors' and user_choice == 'paper':
        winner = 'computer'
    return winner

def get_user_choice():
    user_choice = input('Enter rock, paper, or scissors: ')
    return user_choice


def play_again():
    again = input('Play again? (y/n): ')
    return again


main()