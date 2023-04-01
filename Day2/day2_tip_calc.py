print("welcome to the tip calculator.")
bill = input("what is the total bill?")
percent = input("what percentage tip would you like to give ?10,12,or15?")
people = input("how many people to split the bill?")
pre = 1 + float(percent) / 100
spiltBill = round((int(bill) * pre) / int(people), 2)
print(f"Each person should pay:${spiltBill}")
