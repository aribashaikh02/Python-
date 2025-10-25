x= int(input("enter the book price:"))
y= int(input("enter the book count:"))

total_cost=x*y
print("total cost is ",total_cost)
money= float(input("enter your money status "))

remaining= money-total_cost
print ("Remaining money left is",remaining)