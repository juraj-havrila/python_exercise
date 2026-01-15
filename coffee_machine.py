from tkinter import Menu
from typing import List

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
    "cash":0
}
customer_choice = ""
while customer_choice != exit:
    customer_choice=input("Hello what would you like to have (Expresso/Latte/Cappuccino)? ")
    if customer_choice != "Exit" and customer_choice != "Report":
        price=MENU[customer_choice]["cost"]
        print(f"You have ${price} EUR to pay")
        coins_2E=int(input("Insert coins 2EUR: "))
        coins_1E=int(input("Insert coins 1EUR: "))
        coins_50c=int(input("Insert coins 50c: "))
        coins_20c=int(input("Insert coins 20c: "))
        coins_10c=int(input("Insert coins 10c: "))
        customer_paid=2*coins_2E + coins_1E + 0.5*coins_50c + 0.2*coins_20c + 0.1*coins_10c
        missing_ingredient=''
        for ingredient in MENU[customer_choice]["ingredients"]:
            if resources[ingredient] < MENU[customer_choice]["ingredients"][ingredient]:
                missing_ingredient+=ingredient+", "
            #print(f"{ingredient} { MENU[customer_choice]["ingredients"][ingredient]}")
        if missing_ingredient != '':
            print(f"Sorry, the machine run out of {missing_ingredient}")
            print(f"Here is your money back {customer_paid} EUR")
        elif customer_paid < price:
            print(f"Sorry, you paid too little {customer_paid} , {customer_choice} costs {price} EUR")
            print(f"Here is your money back {customer_paid} EUR")
        else:
            change_to_return=customer_paid - price
            print(f"Here is your change {change_to_return} EUR")
            print(f"Enjoy your {customer_choice}")
            resources["cash"]+= price
            for ingredient in MENU[customer_choice]["ingredients"]:
                resources[ingredient] -= MENU[customer_choice]["ingredients"][ingredient]
    if customer_choice != "Report":
        for ingredient in resources:
            print(f"{ingredient} : {resources[ingredient]}")
    if customer_choice == "Exit":
        exit()
