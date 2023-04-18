list1 = input('Enter the first space-separated list of numbers:').split()
list2 = input('Enter the second space-separated list of numbers:').split()

list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]

average = [(list1[i] + list2[i]) / 2 for i in range(len(list1))]

print(average)