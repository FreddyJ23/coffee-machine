MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


# TODO: 4. Check if resources is sufficient to make drink


def is_enough(coffee_ingredients):
    """returns true or false if items are sufficient to make order"""
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"Sorry, not enough {item}")
            return False
    return True


# TODO: 5. Process coins


def coins():
    """calculate total amount of coins put in"""
    quarter = int(input("How many quarters? ")) * 0.25
    dime = int(input("How many dimes? ")) * 0.1
    nickel = int(input("How many nickels? ")) * 0.05
    penny = int(input("How many pennies? ")) * 0.01
    return quarter + dime + nickel + penny


# TODO: 6. Check if transaction is successful
def is_transaction_successful(user_money, coffee_cost):
    """Checks if transaction is successful by returning an addition to profit"""
    if user_money >= coffee_cost:
        change_left = round(user_money - coffee_cost, 2)
        print(f"Here is ${change_left} in change.")
        global profit
        profit += coffee_cost
        return True
    else:
        print("Sorry not enough money. Here is your money back")
        return False


# TODO: 7. Make coffee and deduct from resources


def make_coffee(choice, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {choice}☕. Enjoy!")


is_continue = True
while is_continue:

    # TODO: 1. Prompt the User for coffee choice
    reply = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. Turn off the machine
    if reply == "off":
        is_continue = False
    # TODO: 3. Print report
    elif reply == "report":
        print(
            f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${profit}")
    else:
        drink = MENU[reply]
        if is_enough(drink["ingredients"]):
            user_payment = coins()
            if is_transaction_successful(user_payment, drink["cost"]):
                make_coffee(reply, drink["ingredients"])
