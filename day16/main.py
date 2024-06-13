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

    money_machine.make_payment(ordered_item.cost)
    money_machine.report()


coffee_machine()
