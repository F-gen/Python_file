MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredient):
    """return True when order can be made, Fase is ingredients are insufficient"""
    for item in resources:
        order_ingredient[item] >= resources[item]
        print(f"sorry there is not enough {item}")
        return False
    return True


def process_coins():
    """return total calculated from coins inserted"""
    print("please insert coins")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted,or False if money is insufficient"""





id_on = True

while True:
    choice = input("what would you like?(espresso/latte/cappuccino):")
    if choice == 'off':
        id_on = False
    elif choice == 'report':
        print(f"water{resources['water']}ml")
        print(f"milk{resources['milk']}ml")
        print(f"coffee{resources['coffee']}g")
        print(f"Money{profit}$")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
