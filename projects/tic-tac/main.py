from display import *
from win_chack import *
from validation import *

def main():
    board = [" "] * 9
    current_player = "X"
    while True:
        display_board(board)
        position = get_player_input(current_player, board)
        board[position] = current_player
        if check_winner(board):
            display_board(board)
            display_winner(current_player)
            break
        # elif chack_if_possible_to_win(board,current_player):
        #     display_board(board)
        #     display_winner("Draw")
        #     break
        elif check_draw(board):
            display_board(board)
            display_winner("Draw")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()