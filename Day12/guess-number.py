# 猜数字
# hard 5次机会  easy 10次机会，每输入一次  有对答案对相应提升（too low  too height）

import random

compute_random = random.randint(0, 100)
# print(compute_random, "compute_random")
user_answer = 0


def right(answer):
    if compute_random < answer:
        return "Too height"
    elif compute_random > answer:
        return "Too low"
    else:
        return "right answer"


print("welcome number Guessing Game")
print("I'm thingking of a number between 1 and 100")

type = input("Choose a difficulty.Type 'easy' or 'hard':")

answer_time = 0
if type == "hard":
    answer_time = 10
    print(f"you have {answer_time} chance")
else:
    answer_time = 5
    print(f"you have {answer_time} chance")

while user_answer != compute_random and answer_time != 0:
    answer_time -= 1
    user_answer = int(input("type you answer:"))
    print(f"Now you have {answer_time} chance")
    print(right(user_answer))
