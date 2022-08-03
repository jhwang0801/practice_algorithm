def selectionSort(arr):
    n = len(arr)

    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]

selectionSort(arr)
print(arr)