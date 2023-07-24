from machine_menu import MENU, resources

money = 0


def call_report():
    for i in resources:
        print(f"{i}:", resources[i])
    print(f"money: ${money:.2f}")


def check_for_ingredients(check_order, from_menu):
    """if it has less resources than it needs, print there's not enough"""
    for i in from_menu:
        if from_menu[i] > resources[i]:
            print(f"There's not enough {i} for your {check_order}, sorry")
            return False
        return True


def check_for_money(check_order, add_money):
    """check_order is the input order | add_money is the money """
    money_in = 0.25 * int(input("Please insert coins.\nHow many quarters?: "))
    money_in += 0.10 * int(input("How many dimes?: "))
    money_in += 0.05 * int(input("How many nickles?: "))
    money_in += 0.01 * int(input("How many pennies?: "))
    if money_in >= MENU[check_order]['cost']:
        add_money += MENU[check_order]['cost']
        if money_in > MENU[check_order]['cost']:
            print(f"here is ${money_in - MENU[check_order]['cost']:.2f} in chane.")
        return True, add_money
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False, add_money


def making_order(check_order):
    for i in resources:
        resources[i] -= MENU[check_order]['ingredients'][i]
    print(f"Here is your {check_order} ☕️. Enjoy!")


'''if order is eiter off or report in this while for order will act different. Otherwise it'll be a key to MENU'''
shut_down_machine = False
while not shut_down_machine:
    '''off to turn of the machine '''
    while True:
        order = input("Please select what type of coffee do you want: ('espresso'/'latte'/'cappuccino'): ").lower()
        if order == 'report':
            call_report()
        if order in ("espresso", "latte", "cappuccino", "off"):
            if order == 'off':
                shut_down_machine = True
            break
    if shut_down_machine:
        break
    has_ingredients = check_for_ingredients(check_order=order, from_menu=MENU[order]['ingredients'])
    if has_ingredients:
        has_money, money = check_for_money(check_order=order, add_money=money)
        if has_money:
            making_order(check_order=order)
