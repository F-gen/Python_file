import random

rock = "👊"
paper = "✋"
scissors = "✂️"
gameImag = [rock, paper, scissors]

hum = int(input("input you decision,0 rock 1 paper 2 scissors"))
if hum >= 3 or hum < 0:
    print("you type an invaild number,you lose")
else:
    print(gameImag[hum])
    com = random.randint(0, 2)
    print(gameImag[com])
    if hum == 0 and com == 2:
        print("You win")
    elif com == 0 and hum == 2:
        print("you lose")
    elif com > hum:
        print("You lose")
    elif com < hum:
        print("You win")
    elif com == hum:
        print("you draw")
