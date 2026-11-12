from display import *
from validations import *
from game_func import *
from file_handler import *






def main():
    while True:
        display_menu()
        choice = user_choice()
        match choice: 
            case 1:
                start_game()
            case 2:
                display_game_history(load_game_history())
            case 3:
                display_statistics(load_game_history())
            case 4:
                print("Exiting the game. Goodbye!")
                break
            case _:
                print("chose between 1-4 only.")


if __name__ == "__main__":
    main()