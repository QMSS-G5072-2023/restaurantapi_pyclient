#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import matplotlib.pyplot as plt
import random

##### first function
##### this function can list all the restaurants in specific location
def query_restaurants_in_location(api_key, location_id, language, currency):
    url = "https://restaurants222.p.rapidapi.com/search"
    payload = {
        "location_id": location_id,
        "language": language,
        "currency": currency,
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "restaurants222.p.rapidapi.com"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to query restaurants. Status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


# In[3]:


##### second function
##### this function can sort restaurants from high ratings to low ratings in a place
def sort_restaurants_by_ratings(api_key, location_id, language, currency):
    # Use the first function to retrieve restaurants in the specified location
    restaurants_in_location = query_restaurants_in_location(api_key, location_id, language, currency)

    if restaurants_in_location and 'results' in restaurants_in_location:
        sorted_restaurants = sorted(
            restaurants_in_location['results']['data'],
            key=lambda x: float(x.get('rating', 0)),
            reverse=True
        )

        if sorted_restaurants:
            print("Sorted Restaurants by Ratings:")
            print("-------------")
            for restaurant in sorted_restaurants:
                print(f"Restaurant Name: {restaurant.get('name')}")
                print(f"Rating: {restaurant.get('rating')}")
                print(f"Price Range: {restaurant.get('price_level')}")
                print("-------------")
        else:
            print("No restaurant data found.")
    else:
        print("Failed to fetch restaurants in the specified location.")


# In[20]:


##### third function
##### this function can get a detailed info about a restaurant
def get_specific_restaurant_details(api_key, restaurant_name, location_id, language, currency):
    url = "https://restaurants222.p.rapidapi.com/search"
    payload = {
        "location_id": location_id,
        "language": language,
        "currency": currency,
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "restaurants222.p.rapidapi.com"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            restaurants_in_location = response.json()
            if restaurants_in_location and 'results' in restaurants_in_location:
                data = restaurants_in_location['results'].get('data', [])
                for restaurant in data:
                    if restaurant.get('name') == restaurant_name:
                        print("Restaurant Details:")
                        print(f"Name: {restaurant.get('name')}")
                        print(f"Rating: {restaurant.get('rating')}")
                        print(f"Price Level: {restaurant.get('price_level')}")
                        print(f"Address: {restaurant.get('address')}")
                        print(f"Phone: {restaurant.get('phone')}")
                        print(f"Website: {restaurant.get('website')}")
                        print("-------------")
                        ## get specific review details
                        reviews = get_reviews_for_location(api_key, restaurant['location_id'], language, currency)
                        if reviews and 'results' in reviews and 'data' in reviews['results']:
                            print("Display All Reviews:")
                            for review in reviews['results']['data']:
                                print(f"Rating: {review.get('rating')}")
                                print(f"Text: {review.get('text')}")
                                print("-------------")
                            # Extract ratings for histogram
                            ratings = [int(review.get('rating')) for review in reviews['results']['data']]
                            if ratings:
                                plt.hist(ratings, bins= 5, range=(1, 6), edgecolor='black')
                                plt.xlabel('Ratings')
                                plt.ylabel('Frequency')
                                plt.title(f"Ratings Histogram for {restaurant_name}")
                                plt.show()
                            else:
                                print("No valid ratings available for histogram.")
                        else:
                            print("No reviews available.")
            else:
                print("Failed to fetch restaurants in the specified location.")
        else:
            print("Failed to query restaurants. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        
 #### third-sub function
 #### this function get restaurants' reviews
def get_reviews_for_location(api_key, location_id, language, currency):
    url = "https://restaurants222.p.rapidapi.com/reviews"

    payload = {
        "location_id": location_id,
        "language": language,
        "currency": currency,
        "offset": "0"
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "restaurants222.p.rapidapi.com"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch reviews. Status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


# In[7]:


##### Fourth Function
##### this function can get the cuisine type of selected restaurant
def get_cuisine_for_restaurant(api_key, restaurant_name, location_id, language, currency):
    url = "https://restaurants222.p.rapidapi.com/search"
    payload = {
        "location_id": location_id,
        "language": language,
        "currency": currency,
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "restaurants222.p.rapidapi.com"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            restaurants_in_location = response.json()
            if restaurants_in_location and 'results' in restaurants_in_location:
                data = restaurants_in_location['results'].get('data', [])
                for restaurant in data:
                    if restaurant.get('name') == restaurant_name:
                        cuisines = restaurant.get('cuisine', [])
                        cuisine_names = [cuisine['name'] for cuisine in cuisines]
                        return cuisine_names
                print(f"No cuisine details found for {restaurant_name}.")
            else:
                print("Failed to fetch restaurants in the specified location.")
        else:
            print("Failed to query restaurants. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    return None


# In[9]:


##### fifth function
##### unlike previous function, this function can list restaurants in a specific cuisine at one location
def search_restaurants_by_cuisine(api_key, cuisine_name, location_id, language, currency):
    url = "https://restaurants222.p.rapidapi.com/search"
    payload = {
        "location_id": location_id,
        "language": language,
        "currency": currency,
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "restaurants222.p.rapidapi.com"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            restaurants_in_location = response.json()
            if restaurants_in_location and 'results' in restaurants_in_location:
                data = restaurants_in_location['results'].get('data', [])
                matching_restaurants = []
                for restaurant in data:
                    cuisines = [cuisine['name'].lower() for cuisine in restaurant.get('cuisine', [])]
                    if cuisine_name.lower() in cuisines:
                        matching_restaurants.append(restaurant)
                if matching_restaurants:
                    return matching_restaurants
                else:
                    print(f"No restaurants found with {cuisine_name} cuisine.")
            else:
                print("Failed to fetch restaurants in the specified location.")
        else:
            print("Failed to query restaurants. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    return None


# In[11]:


##### sixth function
##### this question can generate a random restaurant in assigned location
def get_random_restaurant(api_key, location_id, language, currency):
    url = "https://restaurants222.p.rapidapi.com/search"
    payload = {
        "location_id": location_id,
        "language": language,
        "currency": currency,
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "restaurants222.p.rapidapi.com"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            restaurants_in_location = response.json().get('results', {}).get('data', [])
            if restaurants_in_location:
                random_restaurant = random.choice(restaurants_in_location)
                return random_restaurant
            else:
                print("No restaurants found in the specified location.")
        else:
            print("Failed to query restaurants. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    return None

