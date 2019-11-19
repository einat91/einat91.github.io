# 1 Question

import Lib.random as random

random.random()        # Random float x, 0.0 <= x < 1.0
# 0.37444887175646646
random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0
# 1.1800146073117523
random.randint(1, 10)  # Integer from 1 to 10, endpoints included
# 7
random.randrange(0, 101, 2)  # Even integer from 0 to 100
# 26
random.choice('abcdefghij')  # Choose a random element
# 'c'

items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items)
items
[7, 3, 2, 5, 6, 4, 1]

random.sample([1, 2, 3, 4, 5],  3)  # Choose 3 elements
[4, 1, 5]


# 2 Question

def func(x, ans):
    if (x == 0):
        return 0
    else:
        return func(x-1, x+ans)


print(func(2, 0))

# 3 Question

print('search'. find('S'))

# 4 Question
a = (1, 2)
#a[0] += 1

print(a)

# 7 Question
import sys

#input("Enter message")

# 8 Question

str = 's'
print(len(str)) 