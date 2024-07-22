import json
from pprint import pprint

states = None
districts = None
municipalities = None

with open('datasets/states.json', encoding='utf-8') as f:
    states = json.load(f)

with open('datasets/districts.json', encoding='utf-8') as f:
    districts = json.load(f)

with open("datasets/municipalities.json", encoding='utf-8') as file:
    municipalities = json.load(file)


print(districts[0])
