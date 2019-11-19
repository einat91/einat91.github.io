# 1) List:
# General purpose, most widely used data structure
# Grow and shrink size as needed
# Sequence type
# Sortable
# Not-homogenic data types

# 2) Set:
# Store non-duplicate items
# Very fast access vs Lists
# Math Set ops (union, intersect)
# Unordered

# 3) Tuple:
# Immutable (can't add/ change)
# Useful for fixed data
# Faster than Lists
# Sequence type

# 4) Dict: (dictionaries)
# Key/Value pairs
# Associate array, like Java HashMap
# Unordered

# Sequences (String, List, Tuple): Ordered Sets

# Indexing: x[6]
# Slicing: x[1:4]
# Adding/concatenating: +
# Multiplying: *
# Checking membership: in/not in
# Iterating: for i in x:
# len (sequence1)
# min (sequence1)
# max (sequence1)
# sum (sequence1[1:3])
# unpacking = x['pig', 'cow', 'horse']
# a, b, c = x (only when items and variables are equal)
# sorted(list1)
# sequence1.count(item)
# sequence.index(item)

# Lists

# All operations from Sequences, plus:
# constructors:
# x = list()
# x = ['a', 25, 'dog', 8.43]
# x = list(tuple1)
# x = [m for m in range(8)] (o-7)
# x = [z**2 for z in range(10) if z>4]

# del list1[2]: Delete item from list1
# list1.append(item): Appends an item to list1
# list1.extend(sequence1): Appends a sequence to list1
# list1.insert(index,item): Inserts item at index
# list1.pop(): Pops last item
# list1.remove(item): Removes first instance of item
# list1.reverse(): Reverses list order
# list1.sort(): Sorts list in place

# Tuples
# Support all operations for Sequences
# Immutable, but member objects may be mutable
# If the contents of a list shouldn't change, use a tuple to prvent
# items form accidently being added, changed or deleted.
# Tuples are more efficient than lists due to Python's implementation

# Constructors:
# x = (): No-item tuple
# x = (1,2,3)
# x = 1, 2, 3: Parenthesis are optional
# x = 2, : Single-item tuple
# x = tuple(list1): Tuple from list

# Immutable: but member objects may be mutable.
# x = (1,2,3)
# del(x[1]): Error!
# x[1] = 8: Error!
# x = ([1,2], 3): 2-item tuple, list and int
# del(x[0][1]): ([1], 3)

# Sets
# Constructors:
# x = {3, 5, 3, 5}: {5, 3}
# x = set(): Empty set
# x = set(list1): New set from list
# x = set(list1): Strips duplicates
# x = {3*x for x in range(10) if x>5}

# Basic set operations:
# x.add(item): Adds an item to set x
# x.remove(item): Removes an item from set x
# len(x): Gets length of set x
# item in x, item not in x: Checks membership in x
# x.pop(): Pops random item from set x
# x.clear(): Deletes all items from set x

# Standard mathematical set operations:
# Intersection: set1 & set2 (AND)
# Union: set1 | set2 (OR)
# Symmetric Difference: set1 ^ set2 (XOR)
# Difference: set1 - set2 (In set1 but not in set2)
# Subset: set1 <=set2 (set2 contains set1)
# Superset: set1 >= set (set1 contains set2)

# Dictionaries
# Constructors:
# x = {'pork': 25.3, 'beef: 33.8, 'chicken': 22.7}
# x = dict(['pork, 25.3], ['beef': 33.8], ['chicken': 22.7])
# x = dict(pork = 25.3, beef = 33.8, chicken = 22.7)

# Basic dict operations:
# x['beef'] = 25.2: Adds or changes an item in dict x
# del x['beef']: Removes an item from dict x
# len(x): Gets length of dict x
# item in x, item not in x: Checks membership in x (only looks in keys, not values)
# x.clear(): Deletes all items from dict x
# del x: Deletes dict x

# Accessing keys and values in a dict:
# x.keys(): Returns list of keys in x
# x.values(): Returns list of values in x
# x.items(): Returns list of key-value tuple pairs in x
# itme in x.values(): Tests membership in x: returns boolean




