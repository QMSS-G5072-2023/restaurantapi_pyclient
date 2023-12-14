#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from restaurantapi_pyclient import get_specific_restaurant_details
import requests
import matplotlib.pyplot as plt
import random
import os

def test_get_specific_restaurant_details():
    api_key = os.environ.get('RES_API')
    if not api_key:
        print("API key not found in environment variables.")
        return
    
    location_id = '45963'
    language = "en_US"
    currency = "USD"
    restaurant_name = "Zeppola Cafe"

    get_specific_restaurant_details(api_key, restaurant_name, location_id, language, currency)

# Run the test function
test_get_specific_restaurant_details()

