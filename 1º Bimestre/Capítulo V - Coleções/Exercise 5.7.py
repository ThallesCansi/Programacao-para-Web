students = {}
while True:
    name = input("Enter the student's name (or 'end' to close): ")
    if name == 'end':
        break
    grade = float(input('Enter student grade: '))
    students[name] = grade

roundedGrade = {name: round(grade) for name, grade in students.items()}

print(roundedGrade)