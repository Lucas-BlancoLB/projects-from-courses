from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

monetary = MoneyMachine()
my_coffee_maker = CoffeeMaker()
catalog = Menu()


def start_machine():
    while True:
        user_order = input(f"What would you like to order: ({catalog.get_items()}): ").lower()
        if user_order == 'report':
            print(f"Coffee Machine Report:\n{my_coffee_maker.report()}")
            monetary.report()
        elif user_order == 'off':
            user_order =  False
            return user_order, False

        else:
            return catalog.find_drink(user_order), True


while True:
     order, should_i_act = start_machine()
     if not should_i_act: break

     cost = MenuItem.cost(self=catalog.menu[order])
     ingredient_v1 = catalog.menu[order]
     enough_ingredients = my_coffee_maker.is_resource_sufficient(catalog.menu[order])

     if enough_ingredients:
         payment_process = monetary.make_payment(cost=cost)
         if payment_process:
             my_coffee_maker.make_coffee(catalog.menu[order])
