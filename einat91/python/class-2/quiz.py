# Question 1
foo = [8.2, 5.4] * 3
print (foo)

# Question 2
Foo = [ 1,2,3]
Bar = [4,5,6]
Foo.append(Bar)
print(Foo)

# Question 3
List1 = [z+2 for z in range(10) if z>4]
print(List1)

# Question 4
L = ["cat", "dog" ,"mouse"]
del(L[1])
print(L)

# Question 5
L = ["cat", "dog" ,"mouse"]
print(L.pop())
print(L)

# Question 6
#dict1 = {‘tofu’:25.3, 'beef':33.8, 'chicken':22.7}
dict1 = dict([('tofu', 25.3),('beef', 33.8),('chicken', 22.7)])
#dict1 = dict(tofu=25.3, beef=33.8, chicken=22.7)
print(dict1)

# Question 8
Foo = [ 1,2,3]
Bar = [4,5,6]
Foo.extend(Bar)
print(Foo)

# Question 9
X = {5: 'good', 6: 'bad', 1: 'awesome'}
print(X[1])

# Question 10
S1 = {3,5,3,5}
S2 = {5,7}
S = (S1-S2)
print(S)
