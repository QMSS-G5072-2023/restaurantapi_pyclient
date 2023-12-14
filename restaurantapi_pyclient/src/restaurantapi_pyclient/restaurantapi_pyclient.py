#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import matplotlib.pyplot as plt
import random
import os

def query_restaurants_in_location(api_key, location_id, language, currency):
    """
    Queries restaurants in a specific location using the Restaurant API service.

    Args:
    - api_key (str): The API key.
    - location_id (str): The identifier for the location to search nearby restaurants.
    - language (str): The language in which the restaurant information will be provided.
    - currency (str): The currency in which prices will be displayed.

    Returns:
    - dict or None: A dictionary containing restaurant information if successful, else None.

    This function makes a request to the Restaurant API to retrieve information about
    restaurants in a specified location. Imagine one person travels to a new place and didn't 
    know what to eat. This function can list all the restaurants in specific location.
    It uses the provided API key, location ID, language,and currency to form the request 
    and returns the response containing restaurant data.
    """

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


def sort_restaurants_by_ratings(api_key, location_id, language, currency):
    """
    Sorts restaurants in a specified location by their ratings using the Restaurant API service.

    Args:
    - api_key (str): The API key.
    - location_id (str): The identifier for the location to search restaurants in.
    - language (str): The language in which the restaurant information will be provided.
    - currency (str): The currency in which prices will be displayed.

    Prints:
    - Sorted list of restaurants by ratings.

    This function uses the 'query_restaurants_in_location' function to retrieve restaurants
    in the specified location. It then sorts these restaurants based on their ratings in
    descending order and prints the restaurant names, ratings, and price ranges if available.
    If no restaurant data is found or if there's a failure in fetching the restaurants, it
    displays appropriate messages.
    """
    
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


def get_specific_restaurant_details(api_key, restaurant_name, location_id, language, currency):
    
    """
    Retrieves details about a specific restaurant including its reviews and displays a histogram of rating scores.

    Args:
    - api_key (str): The API key.
    - restaurant_name (str): The name of the restaurant to retrieve details for.
    - location_id (str): The identifier for the location to search restaurants in.
    - language (str): The language in which the restaurant information will be provided.
    - currency (str): The currency in which prices will be displayed.

    Prints:
    - Details of the specific restaurant.
    - Reviews for the restaurant.
    - Histogram of rating scores.

    This function fetches restaurant details using the Restaurant API based on the provided
    restaurant name, location ID, language, and currency. It displays specific details about the
    restaurant, retrieves its reviews, prints all of them, and visualizes a histogram of score ratings.
    """
    
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
        
def get_reviews_for_location(api_key, location_id, language, currency):
    """
    Retrieves reviews for a specific location or restaurant.

    Args:
    - api_key (str): The API key.
    - location_id (str): The identifier for the location or restaurant to retrieve reviews for.
    - language (str): The language in which the reviews will be provided.
    - currency (str): The currency in which prices will be displayed.

    Returns:
    - dict or None: A dictionary containing review information if successful, else None.

    This function makes a request to the Restaurant API service to retrieve reviews for a specified
    location or restaurant based on the provided location ID, language, and currency. It returns
    a dictionary containing review data if the request is successful, otherwise returns None.
    """
    
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


def get_cuisine_for_restaurant(api_key, restaurant_name, location_id, language, currency):
    
    """
    Retrieves the cuisine type of a selected restaurant.

    Args:
    - api_key (str): The API key.
    - restaurant_name (str): The name of the restaurant to retrieve cuisine details for.
    - location_id (str): The identifier for the location to search restaurants in.
    - language (str): The language in which the cuisine information will be provided.
    - currency (str): The currency in which prices will be displayed.

    Returns:
    - list or None: A list containing cuisine types of the restaurant if found, else None.

    This function utilizes the first 'query_restaurants_in_location' function to fetch details about
    restaurants in the specified location. It then extracts the cuisine type for the given
    restaurant name using the obtained data and returns a list of cuisine types if available.
    If no cuisine details are found or if there's an error in the process, it returns None.
    """
    
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


def search_restaurants_by_cuisine(api_key, cuisine_name, location_id, language, currency):
    
    """
    Lists restaurants in a specific cuisine at a given location.

    Args:
    - api_key (str): The API key.
    - cuisine_name (str): The name of the cuisine to search for in restaurants.
    - location_id (str): The identifier for the location to search restaurants in.
    - language (str): The language in which the restaurant information will be provided.
    - currency (str): The currency in which prices will be displayed.

    Returns:
    - list or None: A list containing restaurant details with the specified cuisine if found, else None.

    This function queries the Restaurant API service to fetch information about restaurants in the specified
    location. It filters and returns a list of restaurants that serve the provided cuisine name.
    If no restaurants are found for the given cuisine or if an error occurs during the process,
    it returns None.
    """
    
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
##### After seeing all these options, the person still cannot decide which restaurant to go to
##### So this function can generate a random restaurant in assigned location
def get_random_restaurant(api_key, location_id, language, currency):
    
    """
    Generates a random restaurant within a specified location.

    Args:
    - api_key (str): The API key.
    - location_id (str): The identifier for the location to search restaurants in.
    - language (str): The language in which the restaurant information will be provided.
    - currency (str): The currency in which prices will be displayed.

    Returns:
    - dict or None: A dictionary containing details of a randomly selected restaurant if found, else None.

    This function queries the Restaurant API to retrieve information about restaurants in the specified
    location. It randomly selects and returns details of a restaurant from the available list.
    This function is to help users select what to eat if he/she cannot decide. If no restaurants are found 
    in the specified location or if an error occurs during the process, it returns None.
    """
    
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

