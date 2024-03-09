# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# for this challenge, we're going to summarize the earthquake data as follows:
#filter out non-quakes
def notAQuake(seismicEvent):
    if seismicEvent["properties"]["type"] != "earthquake":
        return False
    else:
        return True

earthquakes = list(filter(notAQuake,data["features"]))

# 1: How many quakes are there in total?
print(len(earthquakes))
# 2: How many quakes were felt by at least 100 people?
print(sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100
          for quake in earthquakes))
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def getNumberFelt(quake):
    felt = quake["properties"]["felt"]
    return 0 if felt is None else felt

mostFeltQuake = max(earthquakes,key=getNumberFelt)
print(f'Most felt quake place: {mostFeltQuake["properties"]["place"]} and reports: {mostFeltQuake["properties"]["felt"]}')

# 4: Print the top 10 most significant events, with the significance value of each

def getSignificance(quake):
    significance = quake["properties"]["sig"]
    return 0 if significance is None else significance

earthquakes.sort(key=getSignificance,reverse=True)
for i in range(0,10):
    print(f'Quake {i+1} {earthquakes[i]["properties"]["title"]} with significance {earthquakes[i]["properties"]["sig"]}')

    