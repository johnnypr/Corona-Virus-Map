from geopy import Nominatim 
import json

locator = Nominatim(user_agent='myGeocoder')

with open("datasets\states_titlecase.json",'r') as f:
    jsonFile = json.load(f)

print(type(jsonFile))




for state in jsonFile.keys():
    state_name = jsonFile[state]["name"]
    location = locator.geocode(state_name)
    print(state_name)
    print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
