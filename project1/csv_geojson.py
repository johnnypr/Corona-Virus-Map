import sys
import pandas as pd

def main(csvPath,output=None):
    if output=="":
        output = csvPath.replace(".csv",".json")
    jsonFile = pd.read_csv(csvPath)
    jsonFile = jsonFile.to_json(output)

if __name__ == "__main__":
    csv = sys.argv[1]
    output = str(input("Enter the filename for the geoJson: "))
    main(csv,output)
    