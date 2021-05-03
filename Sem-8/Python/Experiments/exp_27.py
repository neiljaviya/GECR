#Write a python program to retrieve string/s starting with m and having 5
#characters from a) console and b) given file

import sys

#i = sys.argv()
file = open("exp_27.txt")
for line in file:
    if line.startswith('m'):
        if len(line) == 6 and line.endswith("\n"):
            print(line)
        elif len(line) == 5 and not line.endswith("\n"):
            print(line)