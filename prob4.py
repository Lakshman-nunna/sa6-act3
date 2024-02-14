list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6, 7]

intersection = list(filter(lambda number: number in list_1, list_2))

print(intersection)