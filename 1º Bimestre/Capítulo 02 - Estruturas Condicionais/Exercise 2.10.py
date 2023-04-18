g1 = int(input("Enter the grade of the first exam: "))
g2 = int(input("Enter the grade of the second exam: "))
g3 = int(input("Enter the grade of the third exam: "))

average = (g1 + g2 + g3) / 3

if (average == 10):
    print("Congragulations!")
if (average > 6):
    print("You were approved")
else:
    print("Disapproved")