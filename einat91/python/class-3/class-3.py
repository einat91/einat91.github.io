# import os
# OS.func1(...)
# from my_module import my_function1, my_function2
# myfunction2(...)
# import my_module as mm
# mm.function3(...)

# Regular Expressions
# Regular Expressions match patterns in the text. They are more dynamic than searching for specific text.
# They are useful for validating user input, to protect the system/website from a hacker attack.
# (SQL Injection/ HTML Injection).
# They also check that the input is of the expected type and can be used in the program.
# Regular expressions can be used for automatic "Find" or "Find/Search" operations in a script which works with text, for example a text-parsing script.
# Modules are Python scripts (.py extensions), they can be run from other script, and/or run others.

# Import Modules
# Module = python script with .py extension
# Package = folder with Python script(s) and an __init__.py file
# Environement = modules and a Python interpreter which runs them. There
# can be several interpreters and several environments on one computer.
# Virtual enviornment = an environment which is contained in a certain folder
# and runs certain versions of packages. They are useful because some versions of some packages are
# versions of packages. They are useful because some versions of some packages are
# incompatible with each other and/or with the Python interpreter, so you can have the
# specific versions of the packages you need in each enviornment and nothing "Breaks".


# if _name_ == _main_:
#   main()
# The effect on this is that if the current script is being run directly,
# the if condition is True and the main() function is executed.
# If the script is imported and used by another module - the main () function
# of the script is not executed unless called explicitly module_x.run().
#

# random
# math
# sys
# datetime
# calendar

# __ double underscore specific meaning to the interpreter
# if __name__ == __main__:
# main()

# def add_employee(emp, emp_list=None):
#     if emp_list is None:
#         emp_list = []
#     emp_list.append(emp)
#     print(emp_list)


# emps = ['John', 'Jane']

# add_employee('Corey', emps) # adding to an existed list
# add_employee('Dan') # new list
# add_employee('Ted') # appending it to the new list
# Default arguments are evaluated once at the time it creates the function.
# Mutable default argument:
# emp_list=NONE, making sure it's empty.

import Lib.glob
import Lib.html
import time
from Lib.datetime import datetime


def display_time(time=None):
    if time is None:
        time = datetime.now()
    print(time.strftime('%B %D, %Y %H: %M %S'))


display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

names = ['Peter Parker', 'Bruce Wayne', 'Wade Wilson', 'Clark Kent']
heroes = ['Spiderman', 'Batman', 'Deadpool', 'Superman']

# Python 2 and 3 don't work at the same way

identities = zip(names, heroes)
print(identities)
print(list(identities))  # Casint into a list
# zip = zip up the first names in two lists (an iterator)

for identity in identities:
    print('{} is actualy {}!'.format(identity[0], identity[1]))

# Aestriks = importing everying. Hard to debug and casues errors.

print(Lib.html.escape)
print(Lib.glob.escape)
# Best way

# Function parameters with Default Values

def func_append(a, list1=[]):
    list1.append(a)
    print(list1)
# This will not create an empty list1 parameter every time you call the function without
# passing in a variable for list1. If you want an empty list in this scenario you should instead do:


def func_append(a, list1=None):
    if list1 is None:
        list1 = []
    list1.append(a)
    print(list1)

# Packages install: pip

# Regular Expressions (Regexs)


#
