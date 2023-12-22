from models.rating import Rating


class Restaurant:
    restaurants = []

    @property
    def active(self):
        return 'Activated' if self._active else 'Deactivated'

    # The __str__ method is a special method that takes the object and defines that
    # if we need to show that object in text format

    def __str__(self):
        return f'{self._name} | {self._category}'

    # constructor
    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._rating = []
        Restaurant.restaurants.append(self)

    # best practice uses classmethod for method for the class
    # cls is a convention
    @classmethod
    def list_restaurants(cls):
        ''' Lists the restaurants on the list

        Outputs:
            - Displays the list of restaurants on the screen
        '''

        print(f'{'Name'.ljust(22)} | {'Category'.ljust(20)} | Status')

        for restaurant in cls.restaurants:
            print(f'- {restaurant._name.ljust(20)} | {
                  restaurant._category.ljust(20)} | {restaurant.active}')

    # this method is for objects
    def update_status_restaurant_handler(self):
        ''' Update the active/disabled state of a restaurant '''

        self._active = not self._active

    def assign_rating_handler(self, customer, rate):
        rating = Rating(customer, rate)
        self._rating.append(rating)


# print(restaurant_sushi)
# list the attributes, methods of an object
# print(dir(restaurant_sushi))
# list as a dictionary the attributes, methods of an object
# print(vars(restaurant_sushi))
