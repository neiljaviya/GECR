#Write a Python program that counts the number of occurrences of the character in
#the given string. Provide two implementations: recursive and iterative.

def count(s, c) :
	res = 0
	for i in range(len(s)) :
		if (s[i] == c):
			res = res + 1
	return res

str= input("Enter String: ")
c = input("Enter Char to find occurences: ")
print(count(str, c))