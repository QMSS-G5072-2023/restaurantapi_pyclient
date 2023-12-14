#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def test_sort_restaurants_by_ratings(api_key, location_id, language, currency):
    sort_restaurants_by_ratings(api_key, location_id, language, currency)

# Run the test function
api_key = '49f4da63b6msh82906fb62626f36p1967c4jsn7cf7d8a1f72c'
location_id = '45963'
language = "en_US"
currency = "USD"

test_sort_restaurants_by_ratings(api_key, location_id, language, currency)

