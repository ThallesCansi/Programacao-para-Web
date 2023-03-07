students = {}
while True:
    name = input("Enter the student's name (or 'end' to close): ")
    if name == 'end':
        break
    grade = float(input('Enter student grade: '))
    students[name] = grade

approved = {name: grade for name, grade in students.items() if grade >= 7}

print(approved)