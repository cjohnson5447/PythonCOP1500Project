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
#also crashes program if WeatherAPI is down
def get_weather(city):
    try:
        url = c_api_url + "?key=" + api_key + "&q=" + city
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        return {"error": "Network error while getting weather."}

#function for the forecasted weather data
#crashes program if WeatherAPI is down
def forecast(city):
    try:
       url = d_api_url + "?key=" + api_key + "&q=" + city + "&days=1&aqi=no&alerts=no"
       response = requests.get(url)
       response.raise_for_status()
       data = response.json()
       return data
    except requests.exceptions.RequestException:
        return {"error": "Network error while getting weather."}

#function that pulls the sunrise and sunset data
def astronomical(city):
    try:
       url = a_api_url + "?key=" + api_key + "&q=" + city
       response = requests.get(url)
       response.raise_for_status()
       data = response.json()
       return data
    except requests.exceptions.RequestException:
        return {"error": "Network error while getting weather."}