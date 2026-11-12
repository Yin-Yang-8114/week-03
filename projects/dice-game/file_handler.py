import json
import os

def load_game_history(): 
    if not os.path.exists("game_history.json"):
        return []
    try:
        with open("game_history.json", "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        raise IOError(f"Error decoding JSON from game_history.json\n{"YOUR JSON NOT WORKING !"*100000000}")

    
def save_game(game):
    history = load_game_history()
    history.append(game)
    try:
        with open("game_history.json", "w") as file:
            json.dump(history, file, indent=4)
        return True
    except IOError:
        return False

def create_new_game():
    return {
        "player_name":"",
        "rounds": 0,
        "player_score": 0,
        "computer_score": 0,
        "winner": "",
        "results": []}

def adding_round_result_to_game(game, round_number, player_score, computer_score, winner):
    game["results"].append({
        "round": round_number,
        "player_dice": player_score,
        "computer_dice": computer_score,
        "winner": winner})