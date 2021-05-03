#Write a proper email matching regular expression and check the pattern of the email.

import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$' 
email = input("Enter email to be checked: ")

if(re.search(regex, email)):
    print("Valid Email")
else:
    print("Invalid Email")