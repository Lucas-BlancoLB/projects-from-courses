"""I add a new key to MENU/espresso/ingredients/milk with the value 0 — to match the other coffee styles """
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
'''default values water=300; milk=200; coffee=100'''
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
