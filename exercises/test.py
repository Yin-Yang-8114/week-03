import logging
class Coffee:
    def geting():
        user_name = InputValidator.validate_input("Enter your name: ", "str")
        return user_name
class AppLogger:
    @classmethod
    def get_logger(cls, name, log_file = "app.log"):
        logger = logging.getLogger(name)

        if logger.hasHandlers():
            return logger    
        logger.setLevel(logging.DEBUG)        
        formatter = logging.Formatter('%(asctime)s - [%(name)s] - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

# self.logger = AppLogger.get_logger(self.__class__.__name__)
# קריאה בתוך הבנאי שיקבל את השם של הבךשדד אוטמטי או פשוט אפשר להעביר ךלשם ארגומנט אחד וזה גם יעבוד,


class InputValidator:
    @staticmethod
    def get_positive_int(prompt):
        while True:
            user_input = input(prompt)
            try:
                value = int(user_input)
                if value > 0:
                    return value
                print("")
            except ValueError:
                print("")

    @staticmethod
    def get_valid_string(prompt, min_length=1):
        while True:
            user_input = input(prompt).strip()
            if len(user_input) >= min_length:
                return user_input
            print(f"{min_length} ")



class InputValidator:
    logger = AppLogger.get_logger("InputValidator")

    @staticmethod
    def validate_input(message, input_type):
        while True:
            user_input = input(message).strip()
            
            if input_type == "num":
                try:
                    return int(user_input)
                except ValueError:
                    InputValidator.logger.warning(f"Invalid integer input: '{user_input}'")
                    print("please enter a number")
                    
            elif input_type == "positive_num":
                try:
                    value = int(user_input)
                    if value >= 0:
                        return value
                    InputValidator.logger.warning(f"Negative number entered: {value}")
                    print("please enter a positive number")
                except ValueError:
                    InputValidator.logger.warning(f"Invalid positive_num input: '{user_input}'")
                    print("please enter a positive number")
                    
            elif input_type == "str":
                if user_input.replace(" ", "").isalpha():
                    return user_input
                InputValidator.logger.warning(f"Non-alpha string entered: '{user_input}'")
                print("please enter a string")
                
            elif input_type == "not_empty":
                if user_input:
                    return user_input
                InputValidator.logger.warning("Empty string entered.")
                print("cant be empty value")
                
            else:
                error_txt = f"Developer Error: Unknown input_type '{input_type}'"
                InputValidator.logger.error(error_txt)
                raise ValueError(error_txt)


# user_name = InputValidator.validate_input("Enter your name: ", "str" קריאה לפוקנציה




x= Coffee
print(x.geting())
