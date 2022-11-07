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
money = 0.0


def print_report():
    """print Report"""
    print("Water:" + str(resources["water"]) + "ml")
    print("milk:" + str(resources["milk"]) + "ml")
    print("coffee:" + str(resources["coffee"]) + "g")
    print(f"Money: ${money}")


def check_resource(input: str):
    """check resources for given coffee"""
    selected_coffee = MENU[input]
    required_water = selected_coffee["ingredients"]["water"]
    required_milk = selected_coffee["ingredients"]["milk"]
    required_coffee = selected_coffee["ingredients"]["coffee"]
    if required_water is None or required_water < resources["water"]:
        if required_milk is None or required_milk < resources["milk"]:
            if required_coffee is None or required_coffee < resources["coffee"]:
                return True, selected_coffee["cost"]
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough milk")
    else:
        print("Sorry there is not enough water")
    return False, 0.0


def process_coins():
    """gather user input for coin amounts and return the total money value"""
    print("Please input coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    value = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return value


def check_transaction(cost: float, value: float):
    """check if money input is enough to buy the coffee, and update the money in coffee machine accordingly"""
    global money
    if cost > value:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if value > cost:
            change = value - cost
            print(f"Here is ${change} in change.")
        money += cost
        return True


def make_coffee(input: str):
    """dedict the resources required to make the coffee from the coffee machine"""
    selected_coffee = MENU[input]
    required_water = selected_coffee["ingredients"]["water"]
    required_milk = selected_coffee["ingredients"]["milk"]
    required_coffee = selected_coffee["ingredients"]["coffee"]
    if required_water is not None:
        resources["water"] -= required_water
    if required_milk is not None:
        resources["milk"] -= required_milk
    if required_coffee is not None:
        resources["coffee"] -= required_coffee
    print(f"Here is your {input}.Enjoy!")


def run_program():
    prog_cont = True
    while prog_cont:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        if user_input == "off":
            prog_cont = False
            break
        elif user_input == "report":
            print_report()
        else:
            enough_resource, cost = check_resource(user_input)
            if enough_resource:
                money_insert = process_coins()
                if check_transaction(cost, money_insert):
                    make_coffee(user_input)


run_program()




