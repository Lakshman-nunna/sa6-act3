
strings = ['laptop', 'computer', 'apple', 'happy']

compare = sorted(strings, key = lambda x : (len(x) , x))

print(compare)