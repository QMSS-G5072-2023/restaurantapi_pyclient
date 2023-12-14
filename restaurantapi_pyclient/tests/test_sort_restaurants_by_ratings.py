#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from restaurantapi_pyclient import sort_restaurants_by_ratings
import requests
import matplotlib.pyplot as plt
import random
import os

def test_sort_restaurants_by_ratings(location_id, language, currency):
    api_key = os.environ.get('RES_API')
    if not api_key:
        print("API key not found in environment variables.")
        return
    
    sort_restaurants_by_ratings(api_key, location_id, language, currency)

# Run the test function
location_id = '45963'
language = "en_US"
currency = "USD"

test_sort_restaurants_by_ratings(location_id, language, currency)

