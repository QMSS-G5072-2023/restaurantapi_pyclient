# restaurantapi_pyclient

This is a python package that can help users select restaurants given location, cuisine, price range, ratings, etc. When travelling to a new places. People usually don't know what to eat and spend a lot of time to think about which restaurant to go to. This python package has various functions that can help people make better decisions.


## Installation

```bash
$ pip install restaurantapi_pyclient
```

## Functions
`query_restaurants_in_location`

This function queries restaurants in a specific location. Imagine, when you travels to a new place and didn't know what to eat, you can simply use this function to help you. By simply typing your location id, the currency you want to pay, and the language you speak, the function will generates a list of restaurants near you. The list contains the name of the restaurant, its price level, ratings, description and a photo url of it. 


`sort_restaurants_by_ratings`

This function is build upon the first function. After displaying the restaurants nearby, you can also redesign the list of the restaurants. This function helps you rank the restaurant nearby from highest ratings to lowest.


`get_specific_restaurant_details`

Find something attracts you in the above list and want to know more? This function allows you to pick a specific restaurant and provides much more details for that restaurants. The output contains a comprehensive list of all reviews about the specific restaurant as well as a histogram of its rating scores.


`get_cuisine_for_restaurant`

This function is parallel to the above function that can give you a detailed list of how many cuisines that your selected restaurant has.


`search_restaurants_by_cuisine`

Interested in one specific cuisine? This function can help you re-filter the list of restaurants nearby. By selecting a specific cuisine, the output will contains a list of restaurants in your selected cuisine.


`get_random_restaurant`

Still cannot decide what to eat? No worries! This function will help you randomly select a restaurant near you. You only need to type in your location id, the currency you want to pay and the language you speak. Then a randomly selected restaurant will be generated in the output. Enjoy!

## Usage Example

(1) Users can start by fetching restaurants in the nearby location:
```python
from restaurantapi_pyclient import query_restaurants_in_location

api_key = "YOUR_API_KEY"
location_id = "LOCATION_ID"
language = "LANGUAGE_CODE"
currency = "CURRENCY_CODE"

# Fetch restaurants in a location
restaurants = query_restaurants_in_location(api_key, location_id, language, currency)
# Display your nearby restaurants
print(restaurants) 
```

If the user choose location Las Vegas, the currency type to be USD, and English language. Here is an example output:
```python
 """
 Restaurants Nearby:
 Restaurant Name: Zeppola Cafe
 Rating: 5.0
 Price Level: $$ - $$$
 Description: With Zeppola cafe at The Venetian  coming to life, we aim to combine our restaurant experience with our Italian
 love and tradition for the most authentic  pastries and sweets. Not only an exposition of products for the customers to choose
 from ( our bakery side ), but also a full upscale restaurant experience for all of our guests to enjoy. All the way, all day
 long.
 Photo URL: https://media-cdn.tripadvisor.com/media/photo-t/23/87/d7/26/pastries-and-drinks.jpg
 -------------
 Restaurant Name: Primal Steakhouse
 Rating: 5.0
 Price Level: $$$$
 Description: None
 Photo URL: https://media-cdn.tripadvisor.com/media/photo-t/21/70/c1/0f/house-cocktail-at-primal.jpg
 -------------
 ......
 """
```

(2) In addition, they can sort those restaurants by ratings:
```python
from restaurantapi_pyclient import sort_restaurants_by_ratings

api_key = "YOUR_API_KEY"
location_id = "LOCATION_ID"
language = "LANGUAGE_CODE"
currency = "CURRENCY_CODE"

# Sort restaurants by ratings in your nearby locations
sort_restaurants_by_ratings(api_key, location_id, language, currency) 
```

Here is an example output for nearby restaurants in Las Vegas:
```python
 """
 Sorted Restaurants by Ratings:
 -------------
 Restaurant Name: Zeppola Cafe
 Rating: 5.0
 Price Range: $$ - $$$
 -------------
 Restaurant Name: Primal Steakhouse
 Rating: 5.0
 Price Range: $$$$
 -------------
 Restaurant Name: Eggscellent
 Rating: 5.0
 Price Range: $
 -------------
 Restaurant Name: Edge Steakhouse
 Rating: 5.0
 Price Range: $$$$
 -------------
 ......
 """
```

(3) Then users can retrieve specific details about a restaurant, including reviews and a visualized histogram of rating scores:
```python
from restaurantapi_pyclient import get_specific_restaurant_details

api_key = "YOUR_API_KEY"
restaurant_name = "RESTAURANT_NAME"
location_id = "LOCATION_ID"
language = "LANGUAGE_CODE"
currency = "CURRENCY_CODE"

# Display specific restaurant details
get_specific_restaurant_details(api_key, restaurant_name, location_id, language, currency)
```

Here is an example output if user chooses Zeppola Cafe to check more detials:
```python
 """
 Restaurant Details:
 Name: Zeppola Cafe
 Rating: 5.0
 Price Level: $$ - $$$
 Address: 3377 Las Vegas Blvd S #2390, Las Vegas, NV 89109
 Phone: +1 725-204-6595
 Website: https://www.zeppolacafe.com/?y_source=1_OTI5MDA2MzgtNzY5LWxvY2F0aW9uLndlYnNpdGU%3D
 -------------
 Display All Reviews:
 Rating: 3
 Text: The service is so slow and not up to the expectations of a recommended place for breakfast. Cleaning the tables does not
 seem a priority. Not enough personnel makes this place so inefficient. The food is good but looks better than it tastes. I may
 give it another try with hopes they improve because their location is so beautiful.
 -------------
 Rating: 5
 Text: My daughter and I went for dessert and coffee and really enjoyed the food and ambience. The employees are very friendly
 especially the woman who was standing outside seating guests.
 -------------
 Rating: 4
 Text: This spot is ok, the bread is good, but not a big deal, whats best? its location inside The Venetian!
 -------------
 ......
 plus a histogram of rating scores
 """
```

(4) In addition, they can also retrieve the cuisine type of a selected restaurant:
```python
from restaurantapi_pyclient import get_cuisine_for_restaurant

api_key = "YOUR_API_KEY"
restaurant_name = "RESTAURANT_NAME"
location_id = "LOCATION_ID"
language = "LANGUAGE_CODE"
currency = "CURRENCY_CODE"

# Retrieve cuisine for a restaurant
cuisine = get_cuisine_for_restaurant(api_key, restaurant_name, location_id, language, currency)
# Display cuisine types
print(cuisine)  
```

Here is an example output if users want to check the cuisine of Zeppola Cafe:
```python
 """
 Cuisine for Zeppola Cafe: Italian, American, Cafe
 """
```

(5) If users change their mind and want to search restaurants nearby in a specific cuisine:
```python
from restaurantapi_pyclient import search_restaurants_by_cuisine

api_key = "YOUR_API_KEY"
cuisine_name = "CUISINE_NAME"
location_id = "LOCATION_ID"
language = "LANGUAGE_CODE"
currency = "CURRENCY_CODE"

# Search restaurants by cuisine
restaurants_by_cuisine = search_restaurants_by_cuisine(api_key, cuisine_name, location_id, language, currency)
# Display restaurants with the specified cuisine
print(restaurants_by_cuisine) 
```

Here is an example output if users want to choose American cuisine restaurants nearby:
```python
 """
 Restaurants with American cuisine:
 Name: Zeppola Cafe
 Rating: 5.0
 Price Level: $$ - $$$
 -------------
 Name: Primal Steakhouse
 Rating: 5.0
 Price Level: $$$$
 -------------
 Name: Eggscellent
 Rating: 5.0
 Price Level: $
 -------------
 Name: Edge Steakhouse
 Rating: 5.0
 Price Level: $$$$
 -------------
 ......
 """
```

(6) After seeing all these details, if users still cannot decide what to it. Here is a function that can help them! This function will help people randomly select a restaurant nearby to go for:
```python 
from restaurantapi_pyclient import get_random_restaurant

api_key = "YOUR_API_KEY"
location_id = "LOCATION_ID"
language = "LANGUAGE_CODE"
currency = "CURRENCY_CODE"

# Generate a random restaurant
random_restaurant = get_random_restaurant(api_key, location_id, language, currency)
# Display details of the randomly selected restaurant and enjoy!
print(random_restaurant)  
```

Here is an example output:
```python
 """
 Can't decide what to eat? Let me decide this for you!
 You're going to ...
 Garrett Popcorn Shops!

 Here are more details of this restaurant:
 Rating: 4.5
 Price Level: $
 Address: 3633 Las Vegas Blvd S Suite 50, Las Vegas, NV 89109-4322
 Phone: +1 888-476-7267
 Website: http://www.garrettpopcorn.com

 Enjoy your time there!
 """
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`restaurantapi_pyclient` was created by Annika Xu. It is licensed under the terms of the MIT license.

## Credits

`restaurantapi_pyclient` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
