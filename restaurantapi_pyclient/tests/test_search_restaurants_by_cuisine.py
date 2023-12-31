#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from restaurantapi_pyclient import search_restaurants_by_cuisine
import requests
import matplotlib.pyplot as plt
import random
import os

def test_search_restaurants_by_cuisine():
    api_key = os.environ.get('RES_API')
    if not api_key:
        print("API key not found in environment variables.")
        return
    
    location_id = '45963'
    language = "en_US"
    currency = "USD"
    cuisine_name = 'American'

    matching_restaurants = search_restaurants_by_cuisine(api_key, cuisine_name, location_id, language, currency)
    if matching_restaurants:
        print(f"Restaurants with {cuisine_name} cuisine:")
        for restaurant in matching_restaurants:
            print(f"Name: {restaurant.get('name')}")
            print(f"Rating: {restaurant.get('rating')}")
            print(f"Price Level: {restaurant.get('price_level')}")
            print("-------------")
    else:
        print(f"No restaurants found with {cuisine_name} cuisine.")

# Run the test function
test_search_restaurants_by_cuisine()

