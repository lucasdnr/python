# FastAPI - Restaurant Menu System

This Python program is an extension of `Restaurant Rating System` where were implemented new functions to create items to restaurant menu and apply discount to the items. We also have a small FastAPI implementation to return the menu of restaurants reading JSON files.

In this document we are only covering the new features, for more details of `Restaurant Rating System` features please visit its documentation

## How to Use

### Running the Application

To run the program, execute the `app.py` file. This can be done by running the following command in your terminal or command prompt:

```
python app.py
```

The program defines a few restaurants and performs operations such as:

 - Update the status of a restaurant (active or disabled) 
 - Assign ratings to restaurants
 - Create a drink, a dish and a dessert and add them to the menu of restaurant
 - Apply a discount to drink and dessert items

### Extract data

This program extract data from the source https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json and save the records into `JSON` files inside `data` folder.

The objective is that these JSON files can function as our data source, no longer needing to consult this endpoint.

To run the program, execute the `extract_data.py` file. This can be done by running the following command in your terminal or command prompt:

```
python extract_data.py
```

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

# Create items of menu
drink_juice = Drink('Orange Juice', 5.0, 'Large')
dish_poutine = MenuDish('Poutine', 2.0, 'The Best Poutine of Country')
cake = Dessert('Cake', 2.99, 'Chocolate Cake', ' ', 'small')

# Apply discounts
drink_juice.apply_discount()
cake.apply_discount()

# Put items to menu
restaurant_sushi.add_item_menu(drink_juice)
restaurant_sushi.add_item_menu(dish_poutine)
restaurant_sushi.add_item_menu(cake)


# Display menu of restaurant
restaurant_sushi.show_menu
```

This example creates two restaurants, updates the status of one of them, assigns ratings, creates items of menu, puts the items to menu, applies discounts in menu items and then displays a list of all items in the restaurant's menu.

## FastAPI

In the `main.py` file we have some endpoints created using the library FastAPI.

### Endpoints

#### 1. `/api/hello`

- **Description:** Basic Hello World endpoint for testing.
- **Method:** GET
- **Example Request:** `http://127.0.0.1:8000/api/hello`
- **Response:**
  ```json
  {"Hello": "World"}
  ```

#### 2. `/api/restaurants/`

- **Description:** Get the menu of restaurants from https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json.
- **Method:** GET
- **Parameters:**
  - `restaurant` (optional): Specify the name of the restaurant to get its menu. If not provided, returns menus of all restaurants.
- **Example Request:**
  - Get menus of all restaurants: `http://127.0.0.1:8000/api/restaurants/`
  - Get menu for a specific restaurant (e.g., KFC): `http://127.0.0.1:8000/api/restaurants/?restaurant=KFC`
- **Response:**
  - If `restaurant` is not specified:
    ```json
    {"Data": [ ... ]}
    ```
  - If `restaurant` is specified:
    ```json
    {"Restaurant": "KFC", "Menu": [ ... ]}
    ```
  - If an error occurs: `{"Error": "status_code - error_message"}`

#### 3. `/api/restaurants-from-files/`

- **Description:** Get the menu of restaurants from local JSON files.
- **Method:** GET
- **Parameters:**
  - `restaurant` (optional): Specify the name of the restaurant to get its menu. If not provided, returns menus of all restaurants.
- **Example Request:**
  - Get menus of all restaurants: `http://127.0.0.1:8000/api/restaurants-from-files/`
  - Get menu for a specific restaurant (e.g., KFC): `http://127.0.0.1:8000/api/restaurants-from-files/?restaurant=KFC`
- **Response:**
  - If `restaurant` is not specified:
    ```json
    [
      {"Restaurant": "Restaurant1", "Menu": [ ... ]},
      {"Restaurant": "Restaurant2", "Menu": [ ... ]},
      ...
    ]
    ```
  - If `restaurant` is specified:
    ```json
    {"Restaurant": "KFC", "Menu": [ ... ]}
    ```
  - If the specified restaurant file is not found: `{"Error": "restaurant not found"}`
  - If an error occurs: `{"Error": "An error occurred"}`

### Running the Application

1. Install the required packages using `pip install -r requirements.txt`.
2. Run the application using `uvicorn main:app --reload`.
