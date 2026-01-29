n=int(input("Enter the number of elements:"))
arr=[0]*n

for i in range(n):
    arr[i]= int(input(f"Enter element[i+1]:"))

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]<arr[j+1]:
            arr[j], arr[j+1]= arr[j+1], arr[j]

print("list:")
print(arr)




