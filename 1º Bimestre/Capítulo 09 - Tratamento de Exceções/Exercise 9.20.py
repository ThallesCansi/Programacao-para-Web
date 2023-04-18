import math

while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            raise ValueError("Negative numbers are not valid.")
        print(f"The square root of {num} is {math.sqrt(num)}")
        break
    except ValueError as e:
        print(f"Error: {e}")