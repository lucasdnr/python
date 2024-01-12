import requests
import json
import os

from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/api/hello')
# ie http://127.0.0.1:8000/api/hello
def hello_world():
    '''
    Basic Hello World for testing route
    '''
    return {'Hello': 'World'}


@app.get('/api/restaurants/')
# ie http://127.0.0.1:8000/api/restaurants/?restaurant=KFC
def get_restaurants(restaurant: str = Query(None)):
    '''
    Get the menu of restaurants from 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    '''

    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        data_json = response.json()
        # if the restaurant parameter is empty or None we will return all data
        # of restaurants
        if restaurant is None:
            return {'Data': data_json}

        data_restaurant = []
        for item in data_json:
            if item['Company'] == restaurant:
                # grouping data of restaurants
                data_restaurant.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurant': restaurant, 'Menu': data_restaurant}
    else:
        return {'Error': f'{response.status_code} - {response.text}'}


@app.get('/api/restaurants-from-files/')
# ie http://127.0.0.1:8000/api/restaurants-from-files/?restaurant=KFC
def get_restaurants(restaurant: str = Query(None)):
    '''
    Get the menu of restaurants from json files
    '''
    data_folder = "data"
    try:
        # if the restaurant parameter is not provided we will read all files otherwise we will
        # look for the specific file of restaurant
        if restaurant is None:
            json_files = [f for f in os.listdir(
                data_folder) if f.endswith(".json")]
            data = {}
            for file in json_files:
                file_path = os.path.join(data_folder, file)
                with open(file_path, 'r') as f:
                    json_data = json.load(f)
                    return {'Restaurant': restaurant, 'Menu': json_data}

        else:
             # If file name is provided, read only that specific JSON file
            file_path = os.path.join(data_folder, restaurant)
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    try:
                        json_data = json.load(f)
                        data[file_name] = json_data
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON in file '{file_name}': {e}")
            else:
                print(f"File '{restaurant}' not found.")
                return {f'Error: {restaurant} not found'}

    except Exception as e:
        print(f'An error occurred: {e}')
        return {f'Error: An error occurred'}
