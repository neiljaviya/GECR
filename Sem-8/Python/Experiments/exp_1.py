#Create a program that asks the user to enter their name and their age. Print out a
#message addressed to them that tells them the year that they will turn 100 years
#old.

name = input("Enter Your Name:")
age = int(input("Enter Your Age:"))
cur_year = 2021
print("Hey %s, you'll turn 100 in %d"%(name, cur_year+(100-age)))