#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

def test_query_restaurants_in_location(location_id, language, currency):
    api_key = os.getenv('RES_KEY')
    restaurants_in_location = query_restaurants_in_location(api_key, location_id, language, currency)

    if restaurants_in_location and 'results' in restaurants_in_location:
        data = restaurants_in_location['results'].get('data', [])
        if data:
            print("Restaurants Nearby:")
            for restaurant in data:
                print(f"Restaurant Name: {restaurant.get('name')}")
                print(f"Rating: {restaurant.get('rating')}")
                print(f"Price Level: {restaurant.get('price_level')}")
                description = restaurant.get('description')
                print(f"Description: {description if description else 'None'}")
                # Accessing photo URL
                photo_url = restaurant.get('photo', {}).get('images', {}).get('thumbnail', {}).get('url')
                print(f"Photo URL: {photo_url if photo_url else 'None'}")
                print("-------------")
        else:
            print("No restaurant data found.")
    else:
        print("Failed to fetch restaurants in the specified location.")

# Test the query_restaurants_in_location function
location_id = '45963'
language = "en_US"
currency = "USD"

test_query_restaurants_in_location(location_id, language, currency)

