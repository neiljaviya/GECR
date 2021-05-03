#Use random library to generate list a and Write one line of Python that takes this
#list a and makes a new list that has only the even elements of this list in it.

import random
a = []
for i in range(random.randint(0,100)):
    a.append(random.randint(0,1000))
new_list = [x for x in a if x % 2 == 0]
print("The randomly generated list has %d numbers."%(len(a)))
print("Total %d even numbers are there which are :"%(len(new_list)),new_list)