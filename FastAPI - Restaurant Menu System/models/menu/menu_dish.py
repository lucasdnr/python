from models.menu.item_menu import ItemMenu

# specifying that the MenuDish class will inherit from the ItemMenu class


class MenuDish(ItemMenu):
    def __str__(self):
        return self._name

    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description

    def apply_discount(self):
        # discount 8%
        self._price -= self._price * 0.08
