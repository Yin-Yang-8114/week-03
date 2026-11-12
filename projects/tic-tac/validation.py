def user_input():
    while True:
        try:
            position = int(input("enter a position (1-9): ")) - 1
            if position < 0 or position > 8:
                print("enter a number between 1 and 9")
            else:
                return position
        except ValueError:
            print("Please enter a number between 1 and 9")

def validate_move(board, position):
    if board[position] == " ":
        return True
    else:
        print("position is already taken")
        return False

def get_player_input(player, board):
    while True:
        print(f"{player}s turn")
        position = user_input()
        if validate_move(board, position):
            return position