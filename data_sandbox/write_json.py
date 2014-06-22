import json

d = {"Food_Trucks": 
         [{"Food_Truck": {"Position": {"Longitude": 122.255, "Latitude": 37.4630},
                          "Name": "Grillenium Falcon"}},
          {"Food_Truck": {"Position": {"Longitude": 122.96233, "Latitude": 37.93368},
                          "Name": "Grill 'Em All"}},
          {"Food_Truck": {"Position": {"Longitude": 122.11499, "Latitude": 37.14496},
                          "Name": "Burger She Wrote"}},
          {"Food_Truck": {"Position": {"Longitude": 122.80592, "Latitude": 37.80404},
                          "Name": "Bon Me"}},
          {"Food_Truck": {"Position": {"Longitude": 122.66089, "Latitude": 37.34253},
                          "Name": "Dogzilla"}}
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