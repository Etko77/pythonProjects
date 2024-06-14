from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Classes to work wit
print("hello")
machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Items
menuItems = menu.get_items()
latte = menuItems[0]
espresso = menuItems[1]
capuccino = menuItems[2]


# Whole process
def coffee_machine():
    print(menu.get_items())
    machine.report()
    money_machine.report()

    order = input("Hello what would you like to order?: ")
    ordered_item = menu.find_drink(order)
    if ordered_item is None:
        print("Error. Invalid item")
        return

    if machine.is_resource_sufficient(ordered_item):
        machine.make_coffee(ordered_item)
        money_machine.make_payment(ordered_item.cost)
    else:
        print(f"Not enough resources")

    money_machine.report()


is_on = True
while is_on:
    coffee_machine()
    off_switch = input("Are you done with your order? [Y/N]")
    if off_switch == "N":
        pass
    elif off_switch == "Y":
        is_on = False
