#A list contain marks of 5 students check and print the result of each students.

marks = [85, 42, 76, 90, 33]
for i in marks:
    if i >= 40:
        print(f"Marks:",i, "-Result: Pass")
    else:
        print(f"Marks:",i, "-Result: Fail")