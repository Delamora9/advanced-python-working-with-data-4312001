# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

quakes = list(x["properties"]["type"] for x in data["features"])

c1 = Counter(quakes)

for et in c1.keys():
    print(f"{et:<15} : {c1[et]:>1}")