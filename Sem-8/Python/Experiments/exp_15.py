#Write a program (function!) that takes a list and returns a new list that contains all 
#the elements of the first list minus all the duplicates. Write two different functions 
#to do this - one using a loop and constructing a list, and another using sets

def loop_list(lst):
  rslt = []
  for x in lst:
    if x not in rslt:
      rslt.append(x)
  rslt.sort()
  return rslt

def set_list(lst):
  return sorted([x for x in set(lst)])

a = [int(x) for x in input("Enter list elem separated by space: ").split()]
print("Unique list elements by looping:",*(x for x in loop_list(a)))
print("Unique list elements by set method:",*(x for x in set_list(a)))