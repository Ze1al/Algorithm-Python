
def SelectSort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
