#Factors. Write a function called getfactors() that takes a single integer as an
#argument and returns a list of all its factors, including 1 and itself.

def getfactors(num):
    return [x for x in range(1,num+1) if num % x == 0]

print(getfactors(100))