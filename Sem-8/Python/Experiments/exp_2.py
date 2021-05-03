#Ask the user for a number. Depending on whether the number is even or odd, print
#out an appropriate message to the user
#    1. If the number is a multiple of 4, print out a different message.
#    2. Ask the user for two numbers: one number to check (call it num) and one
#       number to divide by (check). If check divides evenly into num, tell that to the
#       user. If not, print a different appropriate message.

#take divide_number = 4 for case-1
check_number = int(input("Enter the number of your choice: "))
divide_number = int(input("Enter the number you want to check divisibility: "))
if check_number % divide_number == 0:
    print("Yaay..!! %d is divisible by %d"%(check_number, divide_number))
else:
    print("Naah..!! %d is not divisible by %d"%(check_number, divide_number))