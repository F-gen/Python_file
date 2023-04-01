import random

names = input("Typing name sepreated by ','")
sep_name = names.split(",")
# name_len = len(sep_name)
# pay_person = sep_name[random.randint(0, name_len - 1)]
pay_person = random.choice(sep_name)
print(pay_person + " is going buy")
