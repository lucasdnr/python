# Restaurant Rating System

This Python program implements a simple restaurant rating system using two classes: `Restaurant` and `Rating`. The main purpose of this application is to manage and display information about various restaurants, including their names, categories, activity status, and average ratings.

## How to Use

### Running the Application

To run the program, execute the `app.py` file. This can be done by running the following command in your terminal or command prompt:

```
python app.py
```

The program defines a few restaurants and performs operations such as updating the status of a restaurant (active or disabled) and assigning ratings to restaurants.

### Understanding the Code

#### `Restaurant` Class (in `restaurants.py`)

The `Restaurant` class represents a restaurant and has the following key features:

- **Attributes:**
  - `name`: The name of the restaurant (string).
  - `category`: The category of the restaurant (string).
  - `active`: The status of the restaurant (active or disabled).
  - `rating`: A list of ratings assigned to the restaurant.

- **Methods:**
  - `update_status_restaurant_handler`: Toggles the active/disabled state of a restaurant.
  - `assign_rating_handler`: Registers a review rate for the restaurant.
  - `list_restaurants`: Displays a list of all restaurants along with their categories, average ratings, and status.

#### `Rating` Class (in `rating.py`)

The `Rating` class represents the rating given to a restaurant by a customer. It has two attributes:

- `customer`: The name of the customer who made the review.
- `rate`: The rating given to the restaurant (between 1 and 5).

### Example

```python
# Create instances of restaurants
restaurant_sushi = Restaurant('Yoho', 'Sushi')
restaurant_pizza = Restaurant('Tony', 'Pizza')

# Update the status of a restaurant
restaurant_sushi.update_status_restaurant_handler()

# Assign ratings to a restaurant
restaurant_sushi.assign_rating_handler('Mary', 2)
restaurant_sushi.assign_rating_handler('Deric', 4)

# Display a list of all restaurants
Restaurant.list_restaurants()
```

This example creates two restaurants, updates the status of one of them, assigns ratings, and then displays a list of all restaurants with their information.