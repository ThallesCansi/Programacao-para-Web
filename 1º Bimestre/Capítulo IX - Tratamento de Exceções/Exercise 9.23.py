filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        total = sum(numbers)
        print(f"The sum of the numbers in file '{filename}' is {total}")
except FileNotFoundError:
    print(f"Error: file '{filename}' not found.")
except ValueError:
    print(f"Error: file '{filename}' contains invalid data.")
except:
    print(f"Error: an unexpected error occurred.")