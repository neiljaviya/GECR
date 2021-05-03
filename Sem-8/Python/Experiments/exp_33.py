#Implement classical ciphers using python.

choice = int(input("Caesar - 1\nPlayfair - 2:\n"))

if choice == 1:
    text = input("Enter Plain Text : ")
    s = int(input("Enter Key : "))
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        elif (char == ' '):
            result += ' '
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    print("Encrypted Message: " + result)
    print("Decrypted Message: " + text)

elif choice == 2:
    plaintxt = input("Enter Plain Text: ")
    keytxt = input("Enter Key: ")
    print(keytxt)
    alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    lst = []
    result = []
    plainlst = []

    for char in keytxt:
        if char.upper() in lst:
            continue
        else:
            lst.append(char.upper())

    for a in alphabets:
        if a.upper() in lst:
            continue
        else:
            lst.append(a.upper())


    for txt in plaintxt:
        plainlst.append(txt)

    if len(plainlst) % 2 == 1:
        plainlst.append("Z")

    print()
    x = 0
    for x in range(0,len(plainlst),2):
        l = plainlst[x:x+2]
        i = lst.index(l[0])
        j = lst.index(l[1])

        if i%5 == j%5:
            i=i+5
            j=j+5
        elif int(i/5) == int(j/5):
            if i%5 == 4:
                i = i-4
            else:
                i = i+1
            if j%5 == 4:
                j = j-4
            else:
                j=j+1
        else:
            diff = abs(i%5 - j%5)
            if i%5>j%5:
                i = i - diff
                j = j + diff
            else:
                i = i + diff
                j = j - diff

        x = x+2
        result.append(lst[i])
        result.append(lst[j])
    
    result = ''.join(result)
    print("Encrypted Message:",result)
    plainlst = ''.join(plainlst)
    print("Decrypted Message:",plainlst)