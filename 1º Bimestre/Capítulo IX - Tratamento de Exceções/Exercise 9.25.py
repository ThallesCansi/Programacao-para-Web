class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
def do_something():
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        raise CustomException("An error occurred in do_something().") from e

try:
    do_something()
except CustomException as e:
    print(f"Custom Exception: {e}")
except Exception as e:
    print(f"Generic Exception: {e}")