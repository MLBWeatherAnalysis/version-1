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

games = 'OPSWeatherData.csv'
df = pd.read_csv(games)

data_file = open("data_file3.csv", "w")
data_writer = csv.writer(data_file)

hours_into_the_season = 18
for index, game_day in df.iterrows():
    game = game_day['Game']
    home_team = game_day['Team']
    ops = game_day['OPS']
    team_file = home_team + ".json"
    # find the date/time, pull weather variables
    f = open(team_file)
    row = json.load(f)
    date = row['data'][hours_into_the_season]['timestamp_local'][0:10]
    while date != game:
        hours_into_the_season += 24 # incrementing by hours
        date = row['data'][hours_into_the_season]['timestamp_local'][0:10]

    if date == game:
        # get temp, rain, wind, humidity, pressure, cloud coverage, visibility, and uv rating
        temp = row['data'][hours_into_the_season]['temp']
        rain = round(60 * 0.0393701 * float(row['data'][hours_into_the_season]['precip']), 6) # converted from mm/min to in/hr
        wind = round(2.23694 * float(row['data'][hours_into_the_season]['wind_spd']), 6) # converted from m/s to mph
        humidity = row['data'][hours_into_the_season]['rh'] # as in 32%
        pressure = row['data'][hours_into_the_season]['pres']
        cloud = row['data'][hours_into_the_season]['clouds']
        visibility = row['data'][hours_into_the_season]['vis']
        uv = row['data'][hours_into_the_season]['uv']

        # put this data into the final file with ops
        data = [ops, temp, rain, wind, humidity, pressure, cloud, visibility, uv]
        data_writer.writerow(data)

    f.close()

data_file.close()