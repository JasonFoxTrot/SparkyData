import json

d = {"Food_Trucks": 
         [{"Food_Truck_A": {"Position": {"Longitude": 122.255, "Latitude": 37.4630}}},
          {"Food_Truck_B": {"Position": {"Longitude": 122.96233, "Latitude": 37.93368}}},
          {"Food_Truck_C": {"Position": {"Longitude": 122.11499, "Latitude": 37.14496}}},
          {"Food_Truck_D": {"Position": {"Longitude": 122.80592, "Latitude": 37.80404}}},
          {"Food_Truck_E": {"Position": {"Longitude": 122.66089, "Latitude": 37.34253}}}
          ],
     "Suggestion_Location_Primary": {"Position": {"Longitude": 122.34253, "Latitude": 37.5319},
                                     "Event": {"Type": "Ball Game",
                                               "Position": {"Longitude": 122.80592, "Latitude": 37.66089}},
                                     "Weather": "Sunny"},
     "Suggestion_Location_Secondary": {"Position": {"Longitude": 122.80592, "Latitude": 37.66089},
                                     "Event": {"Type": "Other Food Trucks",
                                               "Position": {"Longitude": 122.80592, "Latitude": 37.66089}},
                                     "Weather": "Partly Cloud"},
    }

with open('sample.json', 'w') as outfile:
  json.dump(d, outfile)