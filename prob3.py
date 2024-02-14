numbers = [1,2,3,4,5]
compare = (lambda x, y: x if x > y else y)

def find_maximum(numbers, compare):
    
    maximum = numbers[0]
    
    for num in numbers:
        maximum = compare(maximum, num)
    
    return maximum


print(find_maximum(numbers, compare))
