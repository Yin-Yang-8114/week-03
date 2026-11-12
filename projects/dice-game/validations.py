def validate_input(message,type):
    while True:
        user_input = input(message).strip()
        if type == "int":
            if user_input.isdigit():
                return int(user_input)
            else:
                print(" Please enter a num")
        if type == "str":
            if user_input.isalpha():
                return user_input
            else:
                print("Please enter a valid string")
        if type == "positive_int":
            if user_input.isdigit() and int(user_input) > 0:
                return int(user_input)
            else:
                print("please enter a positive num")