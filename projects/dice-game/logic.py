def calculate_winner(player_score, computer_score,player_name):
    if player_score > computer_score:
        return f"{player_name}"
    elif computer_score > player_score:
        return "Computer"
    else:
        return "Tie"

def calculating_game_results(game):
    total_player_score = sum(1 for result in game["results"] if result["winner"] == game["player_name"])
    total_computer_score = sum(1 for result in game["results"] if result["winner"] == "Computer")
    game["player_score"] = total_player_score
    game["computer_score"] = total_computer_score
    game["winner"] = calculate_winner(total_player_score, total_computer_score, game["player_name"])
