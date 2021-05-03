#Write a python program to know the current working directory and to print all
#contents of the current directory. What changes we need to make in the program
#if we wish to display the contents of only 'mysub' directory available in current
#directory.

import os

cur = os.getcwd()
print("You are working in",cur)
content = os.listdir()
print("\n\nContent of current directory:\n")
for thing in content:
    print(thing)

subdr = input("\nEnter any subdirectory to see content: ")
if subdr in content:
    subcont = os.listdir(cur+"\\"+subdr)
    print()
    print(subcont)
    print()
else:
    print("No such sub directory")
    print()