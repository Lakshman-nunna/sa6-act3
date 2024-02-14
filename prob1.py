
from functools import reduce
value = 99029
value = str(value)
value = list((value))

sum = reduce(lambda x , y: int(x) + int(y), value)
print(sum)

