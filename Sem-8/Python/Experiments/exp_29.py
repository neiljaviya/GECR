#Write a password generator in Python. Be creative with how you generate
#passwords - strong passwords have a mix of lowercase letters, uppercase letters,
#numbers, and symbols. The passwords should be random, generating a new
#password every time the user asks for a new password. Include your code in a main
#method

import random

print("Generating Strong Password...")
password_item = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz1234567890!@#$%&"
pass_len = range(random.randint(10,16))
password = []
for i in pass_len:
    password.append(random.choice(password_item))

password = ''.join(password)
print("Password is: ",password)