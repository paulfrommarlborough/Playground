""" json load example """

import json

numbers = []
filename='numbers.json'
with open(filename, 'r') as f:
    numbers = json.load( f)

print(f"numbers loaded = {numbers}")    