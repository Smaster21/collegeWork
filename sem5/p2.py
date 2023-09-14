import time
start = time.time()
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

unsorted_list = [89,42,100,93,11,234,30,82,22,75]
sorted_list = selection_sort(unsorted_list)
print(sorted_list)
end = time.time()
print("execution time: ", end - start)
