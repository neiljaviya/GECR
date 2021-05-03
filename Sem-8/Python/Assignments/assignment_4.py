import sys

def string_formatter(lst1, lst2):
    result = []
    for char in lst1:
        for i in range(int(lst2[lst1.index(char)])):
            result.append(char)
    return ''.join(result)

string = sys.argv[1]
numbers = []
letters = []
skip = 0
count = 0
for letter in string:
    if skip != 0:
        skip -= 1
        count += 1
        continue
    if letter.isdigit():
        num = [letter]
        if count != len(string)-1:
            nxt = string[count+1]
            tmp = count
            while nxt.isdigit():
                num.append(nxt)
                skip += 1
                tmp += 1
                if tmp != len(string)-1:
                    nxt = string[tmp+1]
                else:
                    break
        numbers.append(''.join(num))
        count += 1
    elif string[count+1].islower() and string[count].islower():
        letters.append(letter)
        numbers.append('1')
        count += 1
    else:
        letters.append(letter)
        count += 1

print(string_formatter(letters, numbers))