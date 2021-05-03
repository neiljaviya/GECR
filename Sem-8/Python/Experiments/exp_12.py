#Ask the user for a number and determine whether the number is prime or not using 
#function/without function /list comprehensions. 

num = int(input("Enter a number:"))
factors = [x for x in range(1,num) if num%x == 0]
if len(factors)==1:
  print("Number is Prime")
  exit()
print("Number is not Prime")