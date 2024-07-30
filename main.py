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
WATER = resources["water"]
MILK = resources["milk"]
COFFEE = resources["coffee"]
COST = 0
# TODO: 3. Print report


def report(water, milk, coffee, money):
    water_left = WATER - water
    milk_left = MILK - milk
    coffee_left = COFFEE - coffee
    money_left = COST + money
    return f"Water: {water_left}ml\nMilk: {milk_left}ml\nCoffee: {coffee_left}g\nMoney: ${money_left}"


# TODO: 4. Check if resources is sufficient to make drink
    ## create a function collect ingredents from menu and check if they check are above current reources
def is_enough(coffee_type):
    coffee_water = MENU[coffee_type]["ingredients"]["water"]
    coffee_milk = MENU[coffee_type]["ingredients"]["milk"]
    coffee_coffee = MENU[coffee_type]["ingredients"]["coffee"]
    resource_water = resources["water"]
    resource_milk = resources["milk"]
    resource_coffee= resources["coffee"]
    if coffee_water > resource_water:
       print("Sorry there is not enough water.")
    if coffee_milk > resource_milk:
       print("Sorry there is not enough milk.")
    if coffee_coffee > resource_coffee:
       print("Sorry there is not enough coffee.")


# print(report(20, 0, 0, 0))

# TODO: 1. Prompt the User for coffee choice
reply = input("What would you like? (expresso/latte/cappuccino): ").lower()

# TODO: 2. Turn off the machine

is_enough(reply)













