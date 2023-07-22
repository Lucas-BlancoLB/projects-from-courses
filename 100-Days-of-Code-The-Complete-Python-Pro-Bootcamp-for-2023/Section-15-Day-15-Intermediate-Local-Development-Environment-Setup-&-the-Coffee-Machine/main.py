from machine_menu import MENU, resources

money = 0


def call_report():
    for i in resources:
        print(f"{i}:", resources[i])
    print("money:", money)


def check_for_ingredients(check_order):
    """if it has less resources than it needs, print there's not enough"""
    if check_order not in ('report', 'off'):
        check_resources = True
        if MENU[check_order]["ingredients"]["water"] > resources["water"]:
            check_resources = False
            print(f"There's not enough water for your {check_order}, sorry ")
        if MENU[check_order]['ingredients']['milk'] > resources['milk']:
            check_resources = False
            print(f"There's not enough milk for your {check_order}, sorry ")
        if MENU[check_order]['ingredients']['coffee'] > resources['coffee']:
            check_resources = False
            print(f"There's not enough coffee for your {check_order}, sorry ")
        elif check_resources:
            return True


def check_for_money(check_order):
    add_money = 0
    quarter = 0.25 * int(input("Please insert coins.\nHow many quarters?: "))
    dimes = 0.10 * int(input("How many dimes?: "))
    nickles = 0.05 * int(input("How many nickles?: "))
    pennies = 0.01 * int(input("How many pennies?: "))
    money_in = quarter + dimes + nickles + pennies
    if money_in >= MENU[check_order]['cost']:
        add_money += MENU[check_order]['cost']
        money_in -= MENU[check_order]['cost']
        print(f"here is ${money_in:.2f} in change.")
        return True, add_money
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def making_order(check_order):
    for i in resources:
        resources[i] -= MENU[check_order]['ingredients'][i]
    print(f"Here is your {check_order} ☕️. Enjoy!")


'''if order is eiter off or report in this while for order will act different. Otherwise it'll be a key to MENU'''
shut_down_machine = False
while not shut_down_machine:
    '''off to turn of the machine '''
    while True:
        order = input("Please select what type of coffee do you want: ('espresso'/'latte'/'cappuccino')").lower()
        if order == 'report':
            call_report()
        if order in ("espresso", "latte", "cappuccino", "off"):
            if order == 'off':
                shut_down_machine = True
            break
    if shut_down_machine:
        break
    has_ingredients = check_for_ingredients(check_order=order)
    if has_ingredients:
        has_money, money_in_action = check_for_money(check_order=order)
        money += money_in_action
        print(money)
        if has_money:
            making_order(check_order=order)
