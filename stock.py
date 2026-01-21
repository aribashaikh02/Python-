#A list contain stock quantity of 5 products print the stock status.

stock=[0, 5, 15, 50, 100]

for i in stock:
    if i == 0:
        print(f"Stock:", i, "- Out of Stock")
    elif 1 <= i <= 20:
        print(f"Stock:", i, "- Low Stock")
    elif 21 <= i <= 80:
        print(f"Stock:", i, "- In Stock")
    else:
        print(f"Stock:", i, "- Overstocked")