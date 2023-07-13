class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):

        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        #parayı kurus tam seklinde ayarla
        print('''
        We accept the following coins:
        Quarters ($0.25), dimes ($0.10)
        nickles ($0.05), pennies ($0.01)
        ''')
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}? Please: ")) * self.COIN_VALUES[coin]
        print(f'You have provided: {self.CURRENCY}{self.money_received}')
        return self.money_received

    def make_payment(self, cost):
        #para yeterli mi degil mi kontrol et
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
