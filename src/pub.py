class Pub:
    
    def __init__(self, name, till, drinks_list):
        self.name = name
        self.till = till
        self.drinks = drinks_list

    def add_money(self, amount):
        self.till += amount

    def drink_count(self):
        return(len(self.drinks))
        
    def add_drink(self, new_drink):
        self.drinks.append(new_drink)

    def find_drink_by_name(self, name_of_drink):
        for drink in self.drinks:
            if drink.name == name_of_drink:
                return drink

    def sell_drink_to_customer(self, name_of_drink, customer):
        # know which drink object we need
        drink_to_buy = self.find_drink_by_name(name_of_drink)
        # remove money from wallet
        customer.remove_money(drink_to_buy.price)
        # add money to till
        self.add_money(drink_to_buy.price)
