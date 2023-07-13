from menunew import Menu, MenuItem
from coffee_makernew import CoffeeMaker
from money_machinenew import MoneyMachine
from time import sleep


def welcome():
    print('''
           WELCOME TO THE COFFEE MACHINE!
        

          ------ MENU ------ 
          Espresso ($1.50)
          Latte ($2.50)
          Cappuccino ($3.00)
          ------------------

          PS: Type "report" at any moment
          to check our resources available.
          Type "off" to log out from the machine.
        ''')


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    welcome()
    options = menu.get_items()
    user_choice = str(input(f'What would you like?\nOptions ({options}): ')).strip().lower()
    if user_choice == 'off':
        print('<<THE END>>')
        is_on = False
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(user_choice) is None:
        print('Error. Please choose an available option.')
    else:
        beverage = menu.find_drink(user_choice)  # Encapsulates the result
        sufficient_resources = coffee_maker.is_resource_sufficient(beverage)  # TrueFalse result
        sufficient_money = money_machine.make_payment(beverage.cost)
        if sufficient_resources and sufficient_money:
            print('Thank you! Allow us to make your beverage now...')
            coffee_maker.make_coffee(beverage)
            sleep(5)