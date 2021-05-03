import sys

def getfactorsum(num):
    lst = [x for x in range(1,num) if num % x == 0]
    return sum(lst)

l = len(sys.argv)
if l < 3:
    print("Missing required inputs")
    exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

sum1 = getfactorsum(num1)
sum2 = getfactorsum(num2)

if sum1 == num2 and sum2 == num1:
    print("Numbers are Amicable")
else:
    print("Numbers are not Amicable")