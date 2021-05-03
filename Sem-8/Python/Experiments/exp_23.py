#Implement Hashtable with its various functionality.

def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end = " ")

        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")      
        print()

HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)
    print("Value Inserted\n")

def delete(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    if value in Hashtable[hash_key]:
        Hashtable[hash_key].remove(value)
    else:
        print("Value not available\n")

while True:
    query = []
    query = input("Enter Command : (Insert/Delete/Print Key Value)\n").split()
    
    if query[0] == 'Exit' or query[0] == 'exit':
        break
    elif query[0].capitalize() == 'Insert':
        insert(HashTable, int(query[1]), query[2])
    elif query[0].capitalize() == 'Delete':
        delete(HashTable, int(query[1]), query[2])
    elif query[0].capitalize() == 'Print':
        display_hash(HashTable)
    else:
        print("Enter Valid Input")
