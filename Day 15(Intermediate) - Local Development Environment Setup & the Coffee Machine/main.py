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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

user_choice = input("What would you like? (espresso/latte/cappuccino): ")

if user_choice == "report":
    print("Water :" + str(resources["water"]))
    print("Milk :" + str(resources["milk"]))
    print("Coffee :" + str(resources["coffee"]))

elif user_choice == "latte":
    if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
        if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                print("Your latte has been processed!")
                # TODO: update the resources.
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")
    else:
        print("Sorry there is not enough water.")


elif user_choice == "espresso":
    if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
        if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            print("Your espresso has been processed!")
            # TODO: update the resources.
        else:
            print("Sorry there is not enough coffee.")
    else:
        print("Sorry there is not enough water.")

elif user_choice == "cappuccino":
    if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
        if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                print("Your cappuccino has been processed!")
                # TODO: update the resources.
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")
    else:
        print("Sorry there is not enough water.")

else:
    print("worng input!")
