# 质数
n = int(input("check this num:"))


def prime_checker(number):
    count = 0
    for i in range(2, number):
        if number % i == 0:
            count += 1
    if count > 0:
        print("not")
    else:
        print("yes")


prime_checker(number=n)
