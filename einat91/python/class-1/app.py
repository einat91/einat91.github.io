# Python Implementations:
# 1)	CPython: Based on C, deafult implementation
# 2)	Jython: Based on Java, can be executed on Java Virtual Machine.
# 3)	IronPython: Based on #C.
# 4)	Pypy: Subste of Python)
#  * Python > compiler > Python Byetcode > Python Virtual Machine (JVM) > Machine Code

import math
print("Hello World")
print("*" * 10)

# 1)	Static: need to set the type of a variable.
# 2)	Dynamic: setting as a value, it determines in runtime.
# id(): memory location.
# Python Garbage Collector.

student_count = 1000
rating = 4.99
is_published = False
course_name = """
Multiple
Lines
"""

students_count = 1.1
age: int = 20  # Type annoation/ Hinting
# age = "Python" # Incompatible

x = [1, 2, 3]
print(id(x))  # same
x.append(4)
print(id(x))  # same

course = "Python Programming"
print(len(course))  # length of the list
print(course[0])  # first character
print(course[-1])  # last character
print(course[0:3])  # start index to end index
print(course[:3])  # same
print(course[0:])  # the entire string
print(course[:])  # same

# Immutable Types: can't be changes, being located in a different place in the memory.
# Mutable Types: Can be change. For example, a list of object.

print(id(course))
print(id(course[0]))  # primitive types are immutable

# Escape sequences:
# \"
# \'
# \\
# \n

message = """
Python 
Programming
"""
print(message)

first = "Einat"
last = "Ehrlich"
full = f"{len(first)} {last} + {4*7}"  # Concatination

course = "Python Programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("Pro"))
print(course.replace("P", "-"))
print("Programming" not in course)

x = 10  # decimal
x = 0b10  # binary
print(bin(x))  # binary
x = 0x12c  # hexadecimal
print(hex(x))
x = 1 + 2j  # complex numbers: a + bi
print(x)

x = 10 + 3
x = 10 - 3
x = 10 * 3
x = 10 / 3  # floating point
x = 10 // 3  # integer
x = 10 % 3  # modulos
x = 10 ** 3  # power

x = x + 1
x += 1  # augmented assigned operator
# x-- / x++ don't work
print(x)


PI = - 3.14  # Upper case for constant, shouldn't be modified
print(round(PI))  # Round
print(abs(PI))  # Absolut number

# Built-in functions
print(math.floor(PI))

# x = input("x: ")  # input from user, needed to be converted

# Type conversion
print(int(x))
print(float(x))
print(bool(x))
print(str(x))

# Falsy: (will be false in boolean)
# ""
# 0
# [] Empty string
# None (null)

# >=
# ==
# !=

age = 22
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenage")
else:
    print("Child")

print("All done!")

# and, or, not

name = " "

if not name.strip():  # Ignoring white spaces
    print("Name is empty")

age = 22
# Chaining comparison operators
if 18 <= age < 65:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)

# Ternary operator
message = "Eligible" if age >= 18 else "Not eligible"

print(message)

# Loops: For, While

# for x in "Python": # Strings are iterable
#     print(x)
# for x in ['a', 'b'. 'c']:
#     print(x)

# for x in range(0, 10, 2): # last number = step
#     print(x)

# print(type(range(50000))) # range object is iterable
# print([1, 2, 3, 4, 5])

names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break # terminates the iteration
else: # else when there's no breaking
    print ("Not found")

# guess = 0
# answer = 5
# while answer != guess:
#     guess = int(input("Guess: "))

# List = [1, 2, 3]
# Tuple = (1, 2, 3) can be looped

# functions
def increment(number: int, by: int=1) -> tuple:
    return (number, number + by)

   
def save_user(**user): 
    print(user)

save_user(id=1, name="admin") # keyword = multiple variables

# {'id': 1, 'name': 'admin'} Object in JS

# Scope: local and global variables

message = "a" # global
def greet():
    message = "b" # local


greet()
print(message)


print(increment(2))

def multiply(*list): #two spaces
    total = 1
    for number in list:
        total *= number # package as a tuple
    return total

print("start")
print(multiply(1, 2, 3,))
print("finish")

  # Debugging
  # f9 = breakpoint f5 = debugging 
  # f10 = step over f11 = step in
  # shift f11
  # ctrl home end alt shift and drag the sentence

def fizz_buzz(input): 
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

        
print(fizz_buzz(15))

  # divisible by 3 - FIZZ
  # divisible by 5 - BUZZ
  # divisible by 3/5 - FizzBUZZ
  # any - same input


