bill = float(input("Enter the total bill: $"))
tip = float(input("Enter the percentage of tip you want to give:"))
guest_num = int(input("Enter the number of guests:"))
total_bill = bill*(1 + tip/100)
perhead = total_bill/guest_num
print(f"The total bill is {round(total_bill, 2)} and the per head cost is {round(perhead, 2)}")

