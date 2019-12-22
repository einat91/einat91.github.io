# Question 1
import Lib.re as re
import Lib.os as os

str2 = 'Your mission is to read and practice consistently'
regex1 = re.compile("i[\S\s]*t")
print(regex1.findall(str2))

# Question 2

str3 = 'Hi there(greeting). Nice day(a(b)'
remove_parentheses = re.compile(' \ ( [ ^ ( ] + ? \ ) ' )
print(remove_parentheses.sub('', str3))


# Question 3

str1 ="abcde"
reg1 = re.compile('abc|cde')
print(reg1.findall(str1))

# Question 8

str1 = "Bananas Pears Oranges"
reg1 = re.compile('[A-Z]{3,}')
print(reg1.findall(str1))

# Question 9

str1 = "Bananas Pears Oranges"
reg1 = re.compile('(?i)(AN)')
print(reg1.findall(str1))

# Question 10

str1 = "Hope for the best. Prepare for the worst."
reg1 = re.compile('\.\s|\.$')
print(reg1.findall(str1))
