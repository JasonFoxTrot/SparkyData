import json

d = {"Food Trucks": 
         [{"Food Truck A": {"Position": {"Longitude": 125.255, "Latitude": 37.4630}},
          "Food Truck B": {"Position": {"Longitude": 125.96233, "Latitude": 37.93368}},
          "Food Truck C": {"Position": {"Longitude": 125.11499, "Latitude": 37.14496}},
          "Food Truck D": {"Position": {"Longitude": 125.80592, "Latitude": 37.80404}},
          "Food Truck E": {"Position": {"Longitude": 125.66089, "Latitude": 37.34253}}}
          ],
     "Suggestion Location Primary": {"Position": {"Longitude": 125.34253, "Latitude": 37.5319},
                                     "Event": "Ball Game",
                                     "Weather" : "Sunny"},
     "Suggestion Location Secondary": {"Position": {"Longitude": 125.80592, "Latitude": 37.66089},
                                     "Event": "Park",
                                     "Weather" : "Partly Cloud"},
    }

with open('sample.json', 'w') as outfile:
  json.dump(d, outfile)