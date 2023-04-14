while True:
    filename = input("Enter a filename: ")
    
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
        break
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
    except:
        print(f"Error: an unexpected error occurred while reading file '{filename}'.")
        break