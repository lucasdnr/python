import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

# success
if response.status_code == 200:
    data_json = response.json()
    data_restaurants = {}
    for item in data_json:
        name = item['Company']
        if name not in data_restaurants:
            data_restaurants[name] = []
        data_restaurants[name].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })

else:
    print(f'Error {response.status_code}')

for name, data in data_restaurants.items():
    file_name = f'./data/{name}.json'
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
