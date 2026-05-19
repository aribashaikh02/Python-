# Write a program to implement Selection Sort.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]  
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)
