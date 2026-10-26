from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks = Menu()
coffee = CoffeeMaker()
finance = MoneyMachine()

decision = True

while decision:

    order_name = input("What would you like? (espresso/latte/cappuccino): ")

    if order_name.lower() == "report":
        finance.report()
        continue
    elif order_name.lower() == "off":
        print("Turning off the coffee maker")
        decision = False

    # order_item has 3 attributes: name, cost, ingredients
    order_item = drinks.find_drink(order_name)
    if order_item is None:
        continue
    # is_resource_sufficient method requires an input that has ingredients
    if not coffee.is_resource_sufficient(order_item):
        continue

    if not finance.make_payment(order_item.cost):
        continue

    coffee.make_coffee(order_item)