# restaurantapi_pyclient

This is a python package that can help users select restaurants given location, cuisine, price range, ratings, etc. When travelling to a new places. People usually don't know what to eat and spend a lot of time to think about which restaurant to go to. This python package has various functions that can help people make better decisions.
functions. 

## Installation

```bash
$ pip install restaurantapi_pyclient
```

## Functions
`query_restaurants_in_location`
Description: This function queries restaurants in a specific location. Imagine, when you travels to a new place and didn't know what to eat, you can simply use this function to help you. By simply typing your location id, the currency you want to pay, and the language you speak, the function will generates a list of restaurants near you. The list contains the name of the restaurant, its price level, ratings, description and a photo url of it. 


## Usage
To fetch restaurants in a location and sort them by ratings, you can use the following Python code:

```python
from restaurant_utility import query_restaurants_in_location, sort_restaurants_by_ratings

# Your API key, location ID, language, and currency
api_key = "YOUR_API_KEY"
location_id = "LOCATION_ID"
language = "LANGUAGE_CODE"
currency = "CURRENCY_CODE"

# Fetch restaurants in a location
restaurants = query_restaurants_in_location(api_key, location_id, language, currency)

# Sort restaurants by ratings
sort_restaurants_by_ratings(api_key, location_id, language, currency)
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`restaurantapi_pyclient` was created by Annika Xu. It is licensed under the terms of the MIT license.

## Credits

`restaurantapi_pyclient` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
