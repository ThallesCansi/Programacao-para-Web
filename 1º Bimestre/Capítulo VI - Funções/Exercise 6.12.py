list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

intersect = lambda list1, list2: set(list1) & set(list2)

print(list(intersect(list1, list2)))