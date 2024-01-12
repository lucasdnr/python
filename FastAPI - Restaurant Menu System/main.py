from fastapi import FastAPI, Query
import requests

app = FastAPI()


@app.get('/api/hello')
def hello_world():
    '''
    Basic Hello World for testing route
    '''
    return {'Hello': 'World'}


# ie http://127.0.0.1:8000/api/restaurants/?restaurant=KFC
@app.get('/api/restaurants/')
def get_restaurants(restaurant: str = Query(None)):
    '''
    Get the menu of restaurants
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
