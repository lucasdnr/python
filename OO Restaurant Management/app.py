from models.restaurants import Restaurant

restaurant_sushi = Restaurant('Yoho', 'Sushi')
restaurant_sushi.update_status_restaurant_handler()
restaurant_sushi.assign_rating_handler('Mary', 2)
restaurant_sushi.assign_rating_handler('Deric', 4)
restaurant_pizza = Restaurant('Tony', 'Pizza')


def main():
    Restaurant.list_restaurants()


# verifying if python is running or is running as a module
# we can create a hub of applications so we can call this app as a module
if __name__ == '__main__':
    main()
