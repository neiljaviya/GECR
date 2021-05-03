#Implement binary search algorithm to seach name for the given list of names.

def binary_search(arr, low, high, x):

    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1

names = ['Abhi', 'Baban', 'Charana', 'Dev', 'Elliot', 'Fred', 'George', 'Hitarth', 'Ishita', 'Jaime', 'Kyle', 'Lamar', 'Mord', 'Neil', 'Oxford', 'Perry', 'Quester', 'Roger', 'Sanju', 'Tuhar', 'Usha', 'Venessa', 'Wester', 'Xavier', 'Yash', 'Zeel']
data = input("Enter name to in list using binary search: ")
res = binary_search(names, 0, len(names)-1, data.capitalize())
if res != -1:
    print("Name available in list at %d index"%(res))
else:
    print("Name not present in list") 