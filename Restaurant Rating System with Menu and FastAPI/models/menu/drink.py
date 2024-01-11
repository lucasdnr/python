from models.menu.item_menu import ItemMenu

# specifying that the Drink class will inherit from the ItemMenu class


class Drink:
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
