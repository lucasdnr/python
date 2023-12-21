class Restaurant:
    name = ''
    category = ''
    active = False


restaurant_sushi = Restaurant()
restaurant_sushi.name = 'Yoho'
restaurant_sushi.category = 'Sushi'

restaurant_pizza = Restaurant()
restaurant_pizza.name = 'Tony'
restaurant_pizza.category = 'Sushi'

restaurants = [restaurant_sushi, restaurant_pizza]

# print(restaurants)
# list the attributes, methods of an object
# print(dir(restaurant_sushi))
# list as a dictionary the attributes, methods of an object
print(vars(restaurant_sushi))
