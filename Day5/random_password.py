import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y',
          'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the pyPassword Generator!")
nr_letter = int(input("how many letters world you like in your password?\n"))
nr_numbers = int(input("how many letters numbers you like in your password?\n"))
nr_symbols = int(input("how many letters symbols you like in your password?\n"))

# Easy level  固定顺序
password = ""
for char in range(1, nr_letter + 1):
    password += random.choice(letter)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

print(password)
# Hard level  随机顺序
password_list = []
for char in range(1, nr_letter + 1):
    password_list.append(random.choice(letter))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
Hardpassword = ""
for i in password_list:
    Hardpassword += i

print(Hardpassword)
