from geopy import Nominatim 
import json
import csv

locator = Nominatim(user_agent='myGeocoder')

with open("datasets\data-preview.csv",'r') as f:
    reader = csv.reader(f)
    addr = []
    for case in reader:
       if case[1] == 'US':
            if case[0] == "":
                next
            else:
                addr.append("\"{},{}\"".format(case[2],case[3]))

for place in addr:
    print(place)
    location = locator.reverse(place)
    
    print(location.raw)
    # print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

