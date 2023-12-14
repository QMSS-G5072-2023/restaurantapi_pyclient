#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def test_get_specific_restaurant_details(api_key, restaurant_name, location_id, language, currency):
    get_specific_restaurant_details(api_key, restaurant_name, location_id, language, currency)

# Run the test function
api_key = '49f4da63b6msh82906fb62626f36p1967c4jsn7cf7d8a1f72c'
location_id = '45963'
language = "en_US"
currency = "USD"
restaurant_name = "Zeppola Cafe"

test_get_specific_restaurant_details(api_key, restaurant_name, location_id, language, currency)

