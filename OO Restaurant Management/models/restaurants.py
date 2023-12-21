class Restaurant:
    restaurants = []

    # The __str__ method is a special method that takes the object and defines that
    # if we need to show that object in text format
    def __str__(self):
        return f'{self.name} | {self.category}'

    # constructor
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        Restaurant.restaurants.append(self)

    def list_restaurants():
        print(f'{'Name'.ljust(22)} | {'Category'.ljust(20)} | Status')

        for restaurant in Restaurant.restaurants:
            print(f'- {restaurant.name.ljust(20)} | {
                  restaurant.category.ljust(20)} | {restaurant.active}')


restaurant_sushi = Restaurant('Yoho', 'Sushi')
restaurant_pizza = Restaurant('Tony', 'Pizza')
Restaurant.list_restaurants()

# print(restaurant_sushi)
# list the attributes, methods of an object
# print(dir(restaurant_sushi))
# list as a dictionary the attributes, methods of an object
# print(vars(restaurant_sushi))
