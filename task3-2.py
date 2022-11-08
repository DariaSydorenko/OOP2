from datetime import datetime


class PizzaOfTheDay:
    def __init__(self, menu):
        self.menu = menu
        self.price_today = 0

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, menu):
        if not isinstance(menu, dict):
            raise TypeError
        self.__menu = menu

    now = datetime.now()
    day = datetime.weekday(now)

    def pizza_today(self):
        for i in self.menu:
            if i == self.day:
                self.price_today = self.menu[i]["price"]
                return f'Your pizza of thr day is {self.menu[i]["name"]} \nIt`s price: {self.menu[i]["price"]} \n'

    def additional_ingredients(self, ing, ingredients):
        for i in ing:
            for y in ingredients:
                if i == y:
                    self.price_today += ingredients[y] / 50 * ing[i]
        return f'New price with additional ingredients: {self.price_today}'

    def __str__(self):
        return f'{self.menu}'


def main():
    menu = {0: {'name': 'a', 'price': 100},
            1: {'name': 'b', 'price': 90},
            2: {'name': 'c', 'price': 110},
            3: {'name': 'd', 'price': 120},
            4: {'name': 'e', 'price': 105},
            5: {'name': 'f', 'price': 95},
            6: {'name': 'g', 'price': 130}}
    ingredients = {'cheese': 15,           # price for 50 gram
                   'sausage': 20,
                   'meet': 25,
                   'tomato': 10,
                   'salad': 5}
    my_order = PizzaOfTheDay(menu)
    print(my_order.pizza_today())
    print(my_order.additional_ingredients({'tomato': 50, 'sausage': 30, 'meet': 20}, ingredients))


main()

