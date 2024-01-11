from models.restaurants import Restaurant
from models.menu.drink import Drink
from models.menu.menu_dish import MenuDish

restaurant_sushi = Restaurant('Yoho', 'Sushi')
restaurant_sushi.update_status_restaurant_handler()
restaurant_sushi.assign_rating_handler('Mary', 2)
restaurant_sushi.assign_rating_handler('Deric', 4)

drink_juice = Drink('Orange Juice', 5.0, 'Large')
dish_poutine = MenuDish('Poutine', 2.0, 'The Best Poutine of Country')

restaurant_pizza = Restaurant('Tony', 'Pizza')


def main():
    print(drink_juice)
    # Restaurant.list_restaurants()


# verifying if python is running or is running as a module
# we can create a hub of applications so we can call this app as a module
if __name__ == '__main__':
    main()
