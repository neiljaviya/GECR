#Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5
#also perform following task:
#    1. Instead of printing the elements one by one, make a new list that has all the
#       elements less than 5 from this list in it and print out this new list.
#    2. Write this in one line of Python.
#    3. Ask the user for a number and return a list that contains only elements from the
#       original list that are smaller than that number given by the user.

#3
choice_num = int(input("Enter your choice of number: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#1,2
#b = [x for x in a if x < choice_num]
print(*(x for x in a if x < choice_num))