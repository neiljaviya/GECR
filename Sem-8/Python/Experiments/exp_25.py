#Read a text file in Python and print no. of lines and no. of unique words

file = open("accounts.txt")
words = []
for line in file:
    wr = line.split()
    for wor in wr:
        if wor not in words:
            words.append(wor)

print("Total %d unique words found"%(len(words)))