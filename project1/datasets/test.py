import json 


with open("project1\datasets\states_titlecase.json",'r') as f:
    states = json.load(f)

with open("project1\datasets\states.json",'r') as g:
    polygons = json.load(g)

i = 0
for state in states.keys():
    print((polygons['features'][i]['properties']))
    i+=1

