#Write a python program to arrange the characters of a given string 'welcome' 
#in an alphabetical order using insertion sort algorithm.

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

string = input("Enter String of chars to sort them using insertion sort: ")
arr = []
for char in string:
    arr.append(ord(char))

insertionSort(arr)

for i in range(len(arr)):
    arr[i] = chr(arr[i])

print("Charwise sorted string: ",*(x for x in arr))