from models.menu.item_menu import ItemMenu

# specifying that the MenuDish class will inherit from the ItemMenu class


class MenuDish(ItemMenu):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description
