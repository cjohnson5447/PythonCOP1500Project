#current conditions
c_api_url = "http://api.weatherapi.com/v1/current.json"
#forcasted day conditions
d_api_url = "http://api.weatherapi.com/v1/forecast.json"
#astronomical data
a_api_url = "http://api.weatherapi.com/v1/astronomy.json"
#my unique api key
api_key = "22201b829f3b46838d2163913251711"

import requests

#function for the current weather data
def get_weather(city):
   url = c_api_url + "?key=" + api_key + "&q=" + city
   response = requests.get(url)
   data = response.json()
   return data

#function for the forecasted weather data
def forecast(city):
   url = d_api_url + "?key=" + api_key + "&q=" + city + "&days=1&aqi=no&alerts=no"
   response = requests.get(url)
   data = response.json()
   return data

#function that pulls the sunrise and sunset data
def astronomical(city):
   url = a_api_url + "?key=" + api_key + "&q=" + city
   response = requests.get(url)
   data = response.json()
   return data