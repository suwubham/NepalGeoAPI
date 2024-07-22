from typing import Union
import json
from fastapi import FastAPI

provinces = None
districts = None
municipalities = None

with open('datasets/provinces.json', encoding='utf-8') as f:
    provinces = json.load(f)

with open('datasets/districts.json', encoding='utf-8') as f:
    districts = json.load(f)

with open("datasets/municipalities.json", encoding='utf-8') as file:
    municipalities = json.load(file)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/state")
def get_state():
    return provinces


@app.get("/district/{province_id}")
def get_district(province_id: int):
    results = []
    for district in districts:
        if district["province_id"] == province_id:
            results.append(district)

    if results:
        return results

    return {"error": "Province not found"}


@app.get('/municipality/{district_id}')
def get_municipality(district_id):
    results = []
    for municipality in municipalities:
        if municipality["district_id"] == district_id:
            results.append(municipality)

    if results:
        return results

    return {"error": "District not found"}
