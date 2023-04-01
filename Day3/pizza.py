print("welcome to preizz")
size = input("what size pizza you want,S M or L")
add_p = input("do you want add peppa? Y or N")
extra_cheese = input("do you want add peppa? Y or N")
money = 0
if size == 'S':
    money = 15
    if add_p == "Y":
        money += 2
elif size == "M":
    money = 20
    if add_p == "Y":
        money += 3
else:
    money = 25
    if add_p == "Y":
        money += 3

if extra_cheese == "Y":
    money += 1

print(f"Total pizza count is {money}")
