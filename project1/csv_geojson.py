import sys
import pandas as pd
import json



def to_geoJson(jsonData):
    

    csv = pd.read_csv(jsonData)

    print(type(csv))

    jsonObj = csv.to_dict()

    print(type(jsonObj))

    jsonObj = json.dumps(jsonObj)

    jsonObj = json.loads(jsonObj)

    
    print(jsonObj.keys())
#     geojson = {
#     "type": "FeatureCollection",
#     "features": [
#     {
#         "type": "Feature",
#         "geometry" : {
#             "type": "Point",
#             "coordinates": [d["Lon"], d["Lat"]],
#             },
#         "properties" : {
#             "Province/State" : d["Province/State"],
#         "Country/Region": d["Country/Region"],
#         "ConfirmedCases": d["Total"]

#         }
#      } for d in jsonObj.keys()]
# }


    output = open('corona_cases.geojson', 'w')
    json.dump(geojson, output)



if __name__ == "__main__":
    to_geoJson("datasets\data-preview.csv")
