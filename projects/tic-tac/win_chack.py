WINNING_LINES = [(0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6),]

def check_winner(board):
    for line in WINNING_LINES:
        if board[line[0]] == board[line[1]] == board[line[2]] != " ":
            return True
    return False

def check_draw(board):
    if " " not in board:
        return True

# def chack_if_possible_to_win(board,current_player):
#     count =0
#     for line in WINNING_LINES:
#         if (board[line[0]] == board[line[1]] == current_player) and board[line[2]] == " ":
#             count += 1
#         elif (board[line[1]] == board[line[2]] == current_player) and board[line[0]] == " ":
#             count += 1
#         elif (board[line[0]] == board[line[2]] == current_player) and board[line[1]] == " ":
#             count += 1
#     return count ==9


# def check_if_win_possible(board):
#     for line in WINNING_LINES:
#         line_values = [board[line[0]], board[line[1]], board[line[2]]]
#         if not ("X" in line_values and "O" in line_values):
#             return True
#     return False

# def chack_if_possible_to_win(board,current_player):
#     count =0
#     for line in WINNING_LINES:
#         if (board[line[0]] == board[line[1]] == current_player) and board[line[2]] == " ":
#             count += 1
#         elif (board[line[1]] == board[line[2]] == current_player) and board[line[0]] == " ":
#             count += 1
#         elif (board[line[0]] == board[line[2]] == current_player) and board[line[1]] == " ":
#             count += 1
#     return count ==9