#import my_module as mm
import re  # (command line)
import Lib.antigravity
from my_module import find_index, test
import Lib.random as random
import math
import Lib.datetime as datetime
import Lib.calendar as calendar
import Lib.os as os

courses = ['History', 'Math', 'Physics', 'CompSci']

#index = mm.find_index(courses, 'Math')
index = find_index(courses, 'Math')
# print(index)
# print(test)
random_course = random.choice(courses)
rads = math.radians(90)

print(random_course)
print(rads)

today = datetime.date.today()
print(today)
print(calendar.isleap(2017))

# print (os.getcwd()) # Current working directory
# print(os.__file__) # Location of file in file system


# Debugging tools

# Regular Expressions (Regexs)
# Allow us to find a pattern in a specific text

sentence = "My Phone number is 425-341-2591"
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex(sentence)  # match ovject
mo.group()  # returns the actual object

# Grouping with parentheses.
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo.group(1)  # first group
mo.group(2)  # second group
mo.group()  # the whole expression

fruitRegex = re.compile(r'strawberries|blueberries')
mo = fruitRegex.search(sentence)
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')  # ? as *
mo = phoneRegex.search('This is my number 123-456-7890')
mo.group()  # '123-456-7890'
mo = phoneRegex.search('This is mu number 456-7890')
mo.group()  # 456-7890

batRegex = re.compile(r'Bat(wo)*man')  # Batman, Batwomen, or any repetiotion
mo = batRegex.search('I am Batwoman')
mo.group()  # Batman
mo = batRegex.search('I am Batwowowowoman')
mo.group()  # Batwowowoman

batRegex = re.compile(r'Bat(wo)?man')  # Batmen or Batwomen
batRegex = re.compile(r'Bat(wo)+man')  # Batwoman or any repetiotion

# Findall
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex.findall('Amy is 425-214-3121 and Bob is 561-654-3121')
# ['425-214-3121', '561-654-3121']
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
phoneRegex.findall('Amy is 425-214-3121 and Bob is 561-654-3121')
# [('425', '214', '3121'), ('561', '654', '3121')]
# Tuples with three groups

# \D means not a digit: spaces, underscores, letters
# \w means alphanumeric: numbers, letters and underscores
# \W means the opposite, non alphanumeric
# \s means white space character: newline, space, tab, return or form
# + one character or more

regex = re.compile(r'\d+\s\w+')
regex.findall('12 peaches, 15 lemons and 14 cherries')

# Creating a class: vowels
vowelRegex = re.compile(r'[AEIOUaeiou]')
vowelRegex.findall('This is a sentence')
# ['i', 'i', 'a', 'e', 'e', 'e']

# Carrot: Beginning of a sentence ^ 
# Dollar: End of a sentence $

# not including vowels
vowelRegex = re.compile(r'[^AEIOUaeiou]')
vowelRegex.findall('This is a sentence')
# ['T', 'h', 's', ' ', 's', ' ', ' ', 's',

helloRegex = re.compile(r'^Hello')
mo = helloRegex.search('Hello this is bob')
mo.group() # 'Hello'

# raw strings: r'str': ne need to escape the meta characters in the string 
# when writing r before the string
# Meta characters have special meaning and need to be escaped with backslased \t \s.
# When reading text from a file, and testing a pattern on it you could get an encoding error. 
# Fix by using encoding ='utf-8' when reading the file.
# Greedy (default) = matches as much as possible: * or +

# Cheat Sheet
# (?aiLmsux): one or more of the letters can be used as flag(s), e.g: (?i)(pattern) matches
# lower case and upper or a mixture of the pattern which follows.
# The split() and sub() functions.
# \b, a character class which matches a word boundary, is useful
# {m, n} for when you want to have the matches of the character or group between two nums
# finditer(): (not in the cheat sheet), iterates the matches: for match in finditer(pattern,str):

# Method for Easily Writing Regex
# If your regex doesn't match any part of the text you are working on, try using only a part of
# the pattern you want, or using a more general pattern - when you get more maches,
# you can see how to add more parts/ more specifity into the pattern, testing the pattern with each change.

# Python Regular Expressions tips


