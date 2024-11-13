#weather_App
import requests
import pprint 

country = input("enter your area to check weather:")

api_key = "cb771e45ac79a4e8e2205c0ce66ff633" #enter your api code from openweathermap

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+country
weather=requests.get(base_url).json()

pprint.pprint(weather)

