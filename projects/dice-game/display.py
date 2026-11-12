
def display_menu():
    print("================================")
    print("          ROLL DICE")
    print("================================")
    print("1. Start New Game")
    print("2. View Game History")
    print("3. View Statistics")
    print("4. Exit")
    print("\nChoose an option: ")


def display_game_results(game):
    print("================================")
    print("          GAME RESULTS")
    print("================================\n")
    print(f"Player Name: {game['player_name']}")
    print(f"Total Rounds: {game['rounds']}")
    print(f"Player Score: {game['player_score']}")
    print(f"Computer Score: {game['computer_score']}")
    if game["winner"] == "Tie":
        print("The game ended in a tie!")
    else:
        print(f"The winner is: {game['winner']}")


def display_game_history(history):
    if not history:
        print("No game history available.")
        return
    print("================================")
    print("          GAME HISTORY")
    print("================================\n")
    count =0 
    for game in (history):
        count +=1
        print(f"Game {count}:")
        print(f"Player Name: {game['player_name']}")
        print(f"Total Rounds: {game['rounds']}")
        print(f"Player Score: {game['player_score']}")
        print(f"Computer Score: {game['computer_score']}")
        if game["winner"] == "Tie":
            print("The game ended in a tie!")
        else:
            print(f"The winner is: {game['winner']}")
        print("--------------------------------\n")


def display_statistics(history):
    if not history:
        print("No game history available.")
        return
    total_games = len(history)
    player_wins = sum(1 for game in history if game["winner"] != "Computer" and game["winner"] != "Tie")
    computer_wins = sum(1 for game in history if game["winner"] == "Computer")
    ties = sum(1 for game in history if game["winner"] == "Tie")
    
    print("================================")
    print("          STATISTICS")
    print("================================\n")
    print(f"Total Games Played: {total_games}")
    print(f"Player Wins: {player_wins} ({(player_wins / total_games) * 100:.2f}%)")
    print(f"Computer Wins: {computer_wins} ({(computer_wins / total_games) * 100:.2f}%)")
    print(f"Ties: {ties} ({(ties / total_games) * 100:.2f}%)\n")



def print_new_game(player_name, rounds):
    print("================================")
    print("          NEW GAME")
    print("================================")
    print(f"\n player naem : {player_name} \n number of rounds : {rounds} ")


def print_round(round_number):
    print(f"\n           ROUND {round_number}\n")


def display_round_results(player_name, player_score, computer_score, winner):
    print("================================")
    print("          ROUND RESULTS")
    print("================================\n")
    print(f"{player_name} score : {player_score} \ncomputer score : {computer_score} ")
    if winner == "Tie":
        print("It's a tie!")
    else:
        print(f"{winner} wins this round!\n")
  

