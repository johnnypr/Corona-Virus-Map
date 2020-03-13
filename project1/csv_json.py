import pandas as pd 
import sys
import json

def main(csv_file):
    df = pd.read_csv(csv_file)
    for key in df["Province/State"]:
        print(key)

if __name__ == "__main__":
    csv_file = sys.argv[1]
    main(csv_file)
