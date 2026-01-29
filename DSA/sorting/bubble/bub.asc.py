#write a program using bubble sorting in ascending order

arr = [5, 3, 4, 1, 2]

n=len(arr)

for i in range(n-1):
    for j in range(1, n-i):
        if arr[j-1] < arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]

print(arr)
