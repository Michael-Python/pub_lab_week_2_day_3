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

