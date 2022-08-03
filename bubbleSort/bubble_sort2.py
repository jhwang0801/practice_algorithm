def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubbleSort(arr):
    n = len(arr)

    for i in reversed(range(n)):
        for j in range(i):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)

arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print(arr)
