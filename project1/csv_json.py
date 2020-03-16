import pandas as pd 
import sys
import json
import csv 


def main(csv_file,outfile):
    f = open(csv_file, 'r')
    g = json.load('dataset\states.json')
    corona_case = csv.reader(f)
    cases = {}

    with open(outfile,'a') as json_file:
        json_file.write("{\"type\" : \"FeatureCollection\", \"features\" : [")
        for case in reader:
            if case[1] == 'US':
                cases["type"] = "Feature"
                coordinate = [float(case[3]),float(case[2])]
                cases["geometry"] = {"type":"Point","coordinates": coordinate}
                cases["properties"] = {"name": getState(case[0]),'density':int(case[52])}
                json.dump(cases,json_file)
                json_file.write(',')
        json_file.write("]}") 
    


def getState(str_):
    str_ = str_.replace(' ',"")
    str_ = str_.split(',')
    return str_[len(str_)-1]


if __name__ == "__main__":
    csv_file = sys.argv[1]
    outfile = sys.argv[2]
    main(csv_file,outfile)
