import requests
import json
import pandas as pd
import csv

city = ["ARI", "ATL", "BAL", "BOS", "CHC", "CHW", "CIN", "CLE", "COL", "DET", 
        "HOU", "KCR", "LAA", "LAD", "MIA", "MIL", "MIN", "NYM", "NYY", "OAK", 
        "PHI", "PIT", "SDP", "SEA", "SFG", "STL", "TBR", "TEX", "TOR", "WSN"]

coords = {
    "ARI": [33.445278, -112.066944],
    "ATL": [33.89, -84.468],
    "BAL": [39.283889, -76.621667],
    "BOS": [42.34625, -71.09775],
    "CHC": [41.948056, -87.655556],
    "CHW": [41.83, -87.633889],
    "CIN": [39.0975, -84.506667],
    "CLE": [41.495833, -81.685278],
    "COL": [39.756111, -104.994167],
    "DET": [42.339167, -83.048611],
    "HOU": [29.756944, -95.355556],
    "KCR": [39.051, -94.48],
    "LAA": [33.800278, -117.882778],
    "LAD": [34.073611, -118.24],
    "MIA": [25.778056, -80.219722],
    "MIL": [43.028333, -87.971111],
    "MIN": [44.981667, -93.278333],
    "NYM": [40.756944, -73.845833],
    "NYY": [40.829167, -73.926389],
    "OAK": [37.751667, -122.200556],
    "PHI": [39.905833, -75.166389],
    "PIT": [40.446944, -80.005833],
    "SDP": [32.7073, -117.1566],
    "SEA": [47.591, -122.333],
    "SFG": [37.778611, -122.389167],
    "STL": [38.6225, -90.193056],
    "TBR": [27.768333, -82.653333],
    "TEX": [32.747361, -97.084167],
    "TOR": [43.641389, -79.389167],
    "WSN": [38.872778, -77.0075]
}

''' -- IGNORE -- '''
# for each team, get weather data and put in a file
# for i in range(30):
#     # different api keys
#     # "a222d5de136648b180090abd8642fb3f"
#     # "b452f10956ec4907bfcfaf1eeb02079c"
#     #
#     #
#     #
#     for j in range(4, 10):
#         with open(city[i] + ".json", "a") as outfile:
#             api_key = "a222d5de136648b180090abd8642fb3f"
#             lat = coords[city[i]][0]
#             lon = coords[city[i]][1]

#             start_date = ""
#             end_date = ""

#             if j == 9: 
#                 start_date = "2021-09-01"
#                 end_date = "2021-10-05"
#             else:
#                 start_date = "2021-0" + str(j) + "-01"
#                 end_date = "2021-0" + str(j+1) + "-01"
            
#             url = "https://api.weatherbit.io/v2.0/history/hourly?lat=%s&lon=%s&start_date=%s&end_date=%s&tz=local&key=%s&units=I" % (lat, lon, start_date, end_date, api_key)
#             response = requests.get(url)
#             data = json.loads(response.text)

#             json.dump(data, outfile)
''' -- -- '''

for i in range(19,22):
    # different api keys
    # "a222d5de136648b180090abd8642fb3f"
    # "b452f10956ec4907bfcfaf1eeb02079c"
    # "3acefb75cc7a434e932d4bc8b488ed0a"
    # "b6ceebc5363342c6919a45d80b83f9ba"
    #
    api_key = "3acefb75cc7a434e932d4bc8b488ed0a"
    lat = coords[city[i]][0]
    lon = coords[city[i]][1]
    start_date = "2021-04-01"
    end_date = "2021-10-04"
    url = "https://api.weatherbit.io/v2.0/history/hourly?lat=%s&lon=%s&start_date=%s&end_date=%s&tz=local&key=%s&units=I" % (lat, lon, start_date, end_date, api_key)
    response = requests.get(url)
    if response == None or response == '':
        print("Null or empty string value for data in file")
    else:
        data = json.loads(response.text)
    with open(city[i] + ".json", "w") as outfile:
        json.dump(data, outfile)
    # response = urllib.request.urlopen(url)
    # data = response.read()
    # js = json.loads(data.decode("utf-8"))
    
    # with open(city[i] + ".json", "w") as outfile:
    #     json.dump(js, outfile)

# # for each game, get the appropriate weather data and put in final file


# Process: 
# open file associated with home_team
# find appropriate date and time in that file
# pull weather variables
# put in new, final data file
