from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True

while machine_on:
    menu_options = menu.get_items()
    order = input(f"What would you like? {menu_options}: ")
    if order == "off":
        machine_on = False
    # TODO 1: Print report
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # TODO 2: Check resources
        coffee_order = menu.find_drink(order)
        # TODO 3: Process Coins
        # TODO 4: Check order successful
        '''
        we can use this sintax of code
        is_enough_ingredients = coffee_maker.is_resource_sufficient(coffee_order)
        is_payment_successful = money_machine.make_payment(coffee_order.cost)
        if is_enough_ingredients and is_payment_successful:
        '''
        if coffee_maker.is_resource_sufficient(coffee_order) and money_machine.make_payment(coffee_order.cost):
            # TODO 5: Deliver the order
            coffee_maker.make_coffee(coffee_order)




