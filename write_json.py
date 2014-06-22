import json

d = {"hello": "world"}

with open('sample.json', 'w') as outfile:
  json.dump(d, outfile)