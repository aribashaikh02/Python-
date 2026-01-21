#A list contain 7 number, check and print each number is even or odd.

numbers = [12, 7, 9, 20, 33, 42, 55]

for num in numbers:
    if num % 2 == 0:
        print(f"Number:", num, "-Even")
    else:
        print(f"Number:", num, "-Odd")