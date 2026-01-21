#A list contain temperature of 5 days,  print the status of each day.

temperatures = [22.5, 18.0, 25.3, 15.6, 30.2]
for temp in temperatures:
    if temp >= 20:
        print(f"Temperature:", temp, "-Status: Warm")
    else:
        print(f"Temperature:", temp, "-Status: Cold")
