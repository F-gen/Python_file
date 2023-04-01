year = int(input('input the year'))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's leap year")
        else:
            print("It's not leap")
    else:
        print("It's leap year")
else:
    print("It's not leap")
