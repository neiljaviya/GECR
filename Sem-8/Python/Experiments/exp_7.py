#Ask the user for a string and print out whether this string is a palindrome or not.
#Write this program with and without loops(A palindrome is a string that reads the
#same forwards and backwards.)

string = input("Enter string to check:")

l=len(string)
for i in range(0, int(l/2)):
    if string[i] != string[l-i-1]:
        print("String not Palindrome")
        exit()
print("String is Palinfrome checked by looping")

if string[::-1] == string:
    print("String is palindrome checked without loop.")
