
print('Imported my_module...')

import sys

test = 'Test String'

def find_index(to_search, target):
   # Find the index of a value in a sequence
    for i, value in enumerate (to_search):
        if value == target:
            return i

    return -1

#print(sys.path) # directory where i'm running the script from



