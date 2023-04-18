sum = 0

for i in range(2, 100):
    check = 0
    for j in range(2, i):
        if (i % j == 0):
            check += 1
    if (check == 0):
        sum += i

print(sum)