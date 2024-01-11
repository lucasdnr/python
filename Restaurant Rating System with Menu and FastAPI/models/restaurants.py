from models.rating import Rating


class Restaurant:
    '''Represents a restaurant and its characteristics.'''

    restaurants = []

    # The __str__ method is a special method that takes the object and defines that
    # if we need to show that object in text format

    def __str__(self):
        '''Returns a string representation of the restaurant.'''

        return f'{self._name} | {self._category}'

    # constructor
    def __init__(self, name, category):
        '''
        Initializes a Restaurant instance.

        Parameters:
            - name (str): The name of the restaurant.
            - category (str): The category of the restaurant.
        '''

        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._rating = []
        self._menu = []
        Restaurant.restaurants.append(self)

    @property
    def active(self):
        '''Returns a symbol indicating the restaurant's activity status.'''

        return '⌧' if self._active else '☐'

    @property
    def mean_ratings(self):
        '''Calculates and returns the mean rating of the restaurant.'''

        if not self._rating:
            return '-'

        sum_rating = sum(rating._rate for rating in self._rating)
        total_rating = len(self._rating)
        mean = round(sum_rating / total_rating, 1)

        return mean

    # best practice uses classmethod for method for the class
    # cls is a convention
    @classmethod
    def list_restaurants(cls):
        ''' Lists the restaurants on the list

        Outputs:
            - Displays the list of restaurants on the screen
        '''

        print(f'{'Name'.ljust(22)} | {'Category'.ljust(20)} | {
              'Rating'.ljust(20)} | Status')

        for restaurant in cls.restaurants:
            print(f'- {restaurant._name.ljust(20)} | {
                  restaurant._category.ljust(20)} | {str(restaurant.mean_ratings).ljust(20)} | {restaurant.active}')

    # those method is for objects
    def update_status_restaurant_handler(self):
        ''' Update the active/disabled state of a restaurant '''

        self._active = not self._active

    def assign_rating_handler(self, customer, rate):
        '''
        Register a review rate for the restaurant.

        Parameters:
            - customer (str): The name of the customer who made the review.
            - rate (float): The rating given to the restaurant (between 1 and 5).
        '''

        if 0 < rate <= 5:
            rating = Rating(customer, rate)
            self._rating.append(rating)

    def add_drink_to_menu(self, drink):
        self._menu.append(drink)

    def add_dish_to_menu(self, dish):
        self._menu.append(dish)

# código omitido

# print(restaurant_sushi)
# list the attributes, methods of an object
# print(dir(restaurant_sushi))
# list as a dictionary the attributes, methods of an object
# print(vars(restaurant_sushi))
