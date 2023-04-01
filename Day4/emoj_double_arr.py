row1 = ["◼︎", "◼︎", "◼︎"]
row2 = ["◼︎", "◼︎", "◼︎"]
row3 = ["◼︎", "◼︎", "◼︎"]
map_list = [row1, row2, row3]

position = input("input the num")
# print(type(num))
vertical = int(position[1]) - 1
horizonal = int(position[0]) - 1

map_list[vertical][horizonal] = "x"

print(f"{row1}\n{row2}\n{row3}")
