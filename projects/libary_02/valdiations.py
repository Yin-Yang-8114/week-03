from display import display_menu

def user_choice():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        if choice.isdigit() and 1 <= int(choice) <= 8:
            return int(choice)
        else:
            print("invalid choice. please enter a number between 1 and 8.")

def validate_input(message, input_type):
    while True:
        user_input = input(message).strip()
        if input_type == "num":
            if user_input.isdigit():
                return int(user_input)
            else:
                print("please enter a number")
        elif input_type == "positive_num":
            if user_input.isdigit() and int(user_input) >= 0:
                return int(user_input)
            else:
                print("please enter a positive number")
        elif input_type == "str":
            if user_input.isalpha():
                return user_input
            else:
                print("please enter a string")
        elif input_type == "not_empty":
            if user_input.strip():
                return user_input
            else:
                print("cant be empty value")