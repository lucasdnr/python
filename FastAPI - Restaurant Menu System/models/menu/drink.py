from models.menu.item_menu import ItemMenu

# specifying that the Drink class will inherit from the ItemMenu class


class Drink(ItemMenu):
    def __str__(self):
        return self._name

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def apply_discount(self):
        # discount 5%
        self._price -= self._price * 0.05
