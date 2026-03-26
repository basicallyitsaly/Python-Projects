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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

bank = {
    "money": 0,
}


# TODO check if resource sufficient
def resource_check(drink_name):
    needed_water = MENU[drink_name]["ingredients"]["water"]
    needed_coffee = MENU[drink_name]["ingredients"]["coffee"]

    # TODO orders with milk
    if "milk" in MENU[drink_name]["ingredients"]:
        needed_milk = MENU[drink_name]["ingredients"]["milk"]
        if resources["water"] >= needed_water and resources["coffee"] >= needed_coffee and resources["milk"] >= needed_milk:
            return True
            # TODO orders with not enough supplies
        if resources["milk"] < needed_milk:
            print("Sorry, you don't have enough milk")

    # TODO for espresso
    if resources["water"] >= needed_water and resources["coffee"] >= needed_coffee:
        return True
    if resources["water"] < needed_water:
        print("Sorry, you don't have enough water")
    if resources["coffee"] < needed_coffee:
        print("Sorry, you don't have enough coffee")


# TODO Print report
def report():
    print("the current resources are: ")
    print(f"Water : {resources.get('water')} ml.")
    print(f"Milk  : {resources.get('milk')} ml.")
    print(f"Coffee : {resources.get('coffee')} ml.")
    print(f"Money: ${bank['money']}")


# TODO process coins
def process_money():
    print("Please input coins below")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total_cents = (quarters * 25) + (dimes * 10) + (nickles * 5) + (pennies * 1)
    total = total_cents / 100
    return total


# TODO transaction successful
def transaction_money(amount, drink):
    print(f"The amount in total is ${amount}")
    print(f"The price is ${MENU[drink]['cost']}")
    if MENU[drink]["cost"] > amount:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif MENU[drink]["cost"] < amount:
        print("Payment accepted")
        change = round(amount - MENU[drink]['cost'], 2)
        print(f"Here is ${change} dollars in change.")
        return MENU[drink]["cost"]
    elif MENU[drink]["cost"] == amount:
        print("Payment accepted.")
        return amount


# TODO Make Coffee deduct resources
def make_coffee(drink_name):
    print(f"Here is your {drink_name}. Enjoy!")
    needed_water = MENU[drink_name]["ingredients"]["water"]
    needed_coffee = MENU[drink_name]["ingredients"]["coffee"]
    if "milk" in MENU[drink_name]["ingredients"]:
        needed_milk = MENU[drink_name]["ingredients"]["milk"]
        if resources["water"] >= needed_water and resources["coffee"] >= needed_coffee and resources["milk"] >= needed_milk:
            # TODO decrease resources
            resources["water"] -= needed_water
            resources["coffee"] -= needed_coffee
            resources["milk"] -= needed_milk
            return resources["water"], resources["coffee"], resources["milk"]
    else:
        resources["water"] -= needed_water
        resources["coffee"] -= needed_coffee
        return resources["water"], resources["coffee"], resources["milk"]


# TODO what would customer like
serve_coffee = True
while serve_coffee:
    order = input("what would you like? (espresso/latte/cappuccino): ")
    # TODO turn off machine
    if order == "off":
        print("Turning off coffee machine...")
        serve_coffee = False
    elif order == "report":
        report()
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if resource_check(order):
            money_paid = process_money()
            bank["money"] += transaction_money(money_paid, order)
            consumed_tuple = make_coffee(order)
            cons_water, cons_coffee, cons_milk = consumed_tuple
            resources["water"] = cons_water
            resources["coffee"] = cons_coffee
            resources["milk"] = cons_milk
    else:
        print("invalid option try again")
