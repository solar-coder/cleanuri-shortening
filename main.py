# Author: SolarCoder
# Instagram | @solarCoder
import requests
import json

# making a POST request to the CleanURI API Endpoint, with parameters
r = requests.post('https://cleanuri.com/api/v1/shorten', data = {'url':'https://www.instagram.com/solarcoder/'})

# converting response body to JSON
jsoned = r.json()

# reading the json and printing
print(jsoned["result_url"])