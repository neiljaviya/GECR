#Write a python program to append data to an existing file 'python.py'. Read data to
#be appended from the user. Then display the contents of entire file

file = open("python.py", mode='a')

while True:
    ln = input("Append a new line to the file: ")
    if(ln == "exit"):
        break
    file.write(ln+"\n")
    print("Line appended successfully!\n")

file.close()
file = open("python.py", mode='r')

print(file.read())