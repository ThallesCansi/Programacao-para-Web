filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print(f"Error: file '{filename}' not found.")