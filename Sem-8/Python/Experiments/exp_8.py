#Determine if two strings match (without using comparison operators or the cmp()
#built-in function) by scanning each string. Extra credit: Add caseinsensitivity to
#your solution.

(str1,str2) = input("Enter both strings seprated by(,): ").lower().split(',')
(l1,l2) = (len(str1), len(str2))
if l1 == l2:
    for i in range(0, l1):
        if str1[i] != str2[i]:
            print("Both strings are different")
            exit()
    print("Both strings are same")
else:
    print("Both strings are different")