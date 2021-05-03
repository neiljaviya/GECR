#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
#and makes a new list of only the first and last elements of the given list. For 
#practice, write this code inside a function. 

def list_maker(lst):
  return [lst[0], lst[len(lst)-1]]
  
a = input("Enter numbers separated by space: ").split()
b = list_maker(a)
print(*(x for x in b))