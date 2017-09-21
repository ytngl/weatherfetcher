"""
Fetch weather info for a zipcode
Usage: weather_fetcher.py <zipcode>
"""
import requests
import json
import os
from sys import argv

# Users key goes here
key = ""

# Zipcode caught from user input
zipcode = argv[1]

# look-up location
ip = os.popen('curl -s ifconfig.io').read()
ip_location = requests.get('http://ip-api.com/json')
ip_data = json.loads(ip_location.content)


# weather API
parameter = {'key': key, 'q': zipcode}
weather = requests.get("http://api.apixu.com/v1/current.json", params=parameter)

# parsing weather data
w_data = json.loads(weather.content)

# Printing data
print("Location: " + zipcode + " --" + w_data["location"]["name"] + ", " + w_data["location"]["region"])
print("Temperature: " + str(w_data["current"]["temp_c"]) + "C" + "/" + str(w_data["current"]["temp_f"]) + "F")
print("Wind Speed: " + str(w_data["current"]["wind_mph"]) + " mph")
print("Precipitation: " + str(w_data["current"]["wind_mph"]) + " in")
print("Humidity: " + str(w_data["current"]["humidity"]) + "%")
