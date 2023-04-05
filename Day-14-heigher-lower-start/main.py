import art
import game_data
import random

data = game_data.data
print(art.logo)
right = True


def judge(fir, sec):
    if fir > sec:
        return True
    else:
        return False


score = 0

while right:
    if score == 0:
        compare1 = random.randint(0, 50)
        compare2 = random.randint(0, 50)
        if compare1 == compare2:
            compare2 = random.randint(compare1, 50)
    else:
        compare1 = compare2
        compare2 = random.randint(0, 50)

    # print(compare1, compare2, "compare")
    print(f"compareA:{data[compare1]['name']},{data[compare1]['description']},from {data[compare1]['country']}")
    print(art.vs)
    print(f"compareB:{data[compare2]['name']},{data[compare2]['description']},from {data[compare2]['country']}")
    compare1Num = data[compare1]['follower_count']
    compare2Num = data[compare2]['follower_count']
    typing = input("who has more follower?Type 'A' or 'B':")
    if typing == 'A':
        right = judge(compare1Num, compare2Num)
    elif typing == 'B':
        right = judge(compare2Num, compare1Num)

    if right:
        score += 1
        print(f"win,and going on ,score is {score}")

    else:
        print(f"you lose,total score is {score}")
