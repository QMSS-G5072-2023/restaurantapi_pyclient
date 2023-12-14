#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def test_get_random_restaurant():
    api_key = '49f4da63b6msh82906fb62626f36p1967c4jsn7cf7d8a1f72c'
    location_id = '45963'
    language = "en_US"
    currency = "USD"

    random_restaurant = get_random_restaurant(api_key, location_id, language, currency)
    if random_restaurant:
        print("Can't decide what to eat? Let me decide this for you!")
        print("You're going to ...")        
        print(f"{random_restaurant.get('name')}!")
        print()
        print("Here are more details of this restaurant:")   
        print(f"Rating: {random_restaurant.get('rating')}")
        print(f"Price Level: {random_restaurant.get('price_level')}")
        print(f"Address: {random_restaurant.get('address')}")
        print(f"Phone: {random_restaurant.get('phone')}")
        print(f"Website: {random_restaurant.get('website')}")
        print()
        print("Enjoy your time there!")
    else:
        print("Failed to get a random restaurant.")

# Run the test function
test_get_random_restaurant()

