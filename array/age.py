#A list contain age of 5 peoples print the category.
ages = [5, 17, 25, 45, 70]
for age in ages:
    if age < 18:
        print(f"Age:", age, "-Category: Child")
    elif 18 <= age < 60:
        print(f"Age:", age, "-Category: Adult")
    else:
        print(f"Age:", age, "-Category: Senior")
