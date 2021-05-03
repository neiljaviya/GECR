#Write a python program to retrieve name and date of birth (mm-ddyyyy) of
#students from a given file student.txt

import re
fl = open("student.txt", 'r')
data = fl.read()

match = re.search(r'(\d+/\d+/\d+)', data)
print(match.group())