names = input('Enter the space-separated list of names: ').split()
grades = input('Enter the space-separated list of grades: ').split()

grades = [float(grade) for grade in grades]

students = list(zip(names, grades))

ordainedStudents = sorted(students, key = lambda x: x[1], reverse = True)

for student in ordainedStudents:
    print(student)