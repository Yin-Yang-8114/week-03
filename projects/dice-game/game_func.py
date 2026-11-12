from validations import validate_input
from random import randint
from display import *
from logic import calculate_winner,calculating_game_results
from file_handler import *

user_choice = lambda: validate_input("Enter your choice (1-4): ", "positive_int")

def get_player_names():
    player_name = validate_input("Enter your name: ", "str")
    return player_name

def number_of_rounds():
    rounds = validate_input("Enter the number of rounds you want to play (1-10): ", "positive_int")
    if rounds < 1 or rounds > 10:
        print("Please enter a number between 1 and 10.")
        return number_of_rounds()
    return rounds


def roll_dice():
    return randint(1, 6)

def play_round(game):
    player_score = roll_dice()
    computer_score = roll_dice()
    winner = calculate_winner(player_score, computer_score,game["player_name"])
    adding_round_result_to_game(game, len(game["results"]) + 1, player_score, computer_score, winner)
    display_round_results(game["player_name"], player_score, computer_score, winner)


def start_game():
    game = create_new_game()
    game["player_name"] = get_player_names()
    game["rounds"] = number_of_rounds()
    print_new_game(game["player_name"], game["rounds"])
    for round_number in range(1, game["rounds"] + 1):
        print_round(round_number)
        play_round(game)
    calculating_game_results(game)
    display_game_results(game)
    save_game(game)







