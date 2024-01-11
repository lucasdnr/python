from models.menu.item_menu import ItemMenu


class Dessert(ItemMenu):
    def __init__(self, name, price, description, type, size):
        super().__init__(name, price)
        self.description = description
        self.type = type
        self.size = size

    def __str__(self):
        return self._name

    def apply_discount(self):
        # discount 15%
        self._price -= self._price * 0.15
