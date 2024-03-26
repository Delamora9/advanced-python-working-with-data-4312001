# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
header = ["Magnitude", "Place", "Felt Reports", "Date", "Google Map link"]
rows = []

def getSig(event):
    significance = event["properties"]["sig"]
    return 0 if significance is None else significance

data["features"].sort(key=getSig, reverse=True)
for i in range(0,41):
    event = data["features"][i]
    thedate = datetime.date.fromtimestamp(
                    int(event["properties"]["time"])/1000)
    mapslink = "https://www.google.com/maps/search/?api=1&query="
    mapslink += str(event["geometry"]["coordinates"][1]) + "%2C"
    mapslink += str(event["geometry"]["coordinates"][0])
    rows.append([event["properties"]["mag"],
                event["properties"]["place"],
                event["properties"]["felt"],
                thedate,
                mapslink])

def getDate(row):
    return row[3]
rows.sort(key=getDate,reverse=True) 
with open("significantsesimicevents.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(rows)