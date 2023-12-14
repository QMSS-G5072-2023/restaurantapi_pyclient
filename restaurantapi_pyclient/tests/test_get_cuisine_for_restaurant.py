#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

def test_get_cuisine_for_restaurant():
    api_key = os.environ.get('RES_API')
    if not api_key:
        print("API key not found in environment variables.")
        return
    
    location_id = '45963'
    language = "en_US"
    currency = "USD"
    restaurant_name = "Zeppola Cafe"

    cuisine_info = get_cuisine_for_restaurant(api_key, restaurant_name, location_id, language, currency)
    print(f"Cuisine for {restaurant_name}: {', '.join(cuisine_info)}")

# Run the test function
test_get_cuisine_for_restaurant()

