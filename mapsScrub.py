import requests
from bs4 import BeautifulSoup

# set up the Google Maps API URL
url = "https://maps.google.com/maps/api/place/nearbysearch/json"

# set up the parameters for the API request
params= {
    "location": "37.7749, -122.4194", # latitude , logitude of the location you want
    "radius": "1000", # radius in meters
    "type": "restaurant", #the type of place you want to search for
    "key": "YOUR_API_KEY", # your Google Maps API key 
}

# make the API requests
response= requests.get(url, params=params)

# extract the HTML response using Beatiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# extract the relevant information fro, the HTML response
for result in soup.find_all('result'):
    name = result.find('name').text
    address =  result.find('vicinity').text
    print(f"{name} - {address}")