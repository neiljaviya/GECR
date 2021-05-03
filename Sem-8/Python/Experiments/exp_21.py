#Implement bubble sort algorithhm

def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [int(x) for x in input("Enter space separated nums to bubblesort:\n").split()]

bubbleSort(arr)

print ("Sorted nums:",*(x for x in arr))