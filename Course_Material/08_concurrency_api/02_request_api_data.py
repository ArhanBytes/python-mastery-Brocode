"""
Topic: Request API data
Section: Concurrency and API
Description:
Demonstrates how to connect to an API in Python using the requests module,
send a GET request, handle the response, and extract JSON data into a dictionary.
"""

import requests

base_url = "https://pokeapi.co/api/v2"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)  # module->function it returns a response object

    if response.status_code == 200:
        # response is in json format by using json() it will convert it to python dectionary
        pokemon_data = response.json()  # object->method
        return pokemon_data
    else:
        print(f"Error {response.status_code}: Failed to retrieve data")
    print(response)


pokemon_name = "mewtwo"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}cm")
    print(f"Weight: {pokemon_info['weight']}hg")
