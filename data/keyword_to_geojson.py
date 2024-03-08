import pandas as pd
import json
import os

#path = "D:/Desktop/TESI/Dati 19-02-2024/"
path = os.path.dirname(os.path.realpath(__file__))+"/"

keys = pd.read_csv(path+'keywords_coordinates.csv', delimiter=',', low_memory=False)

geojson = {}
geojson["type"] = "FeatureCollection"
geojson["name"] = "LIST"
geojson["features"] = []

for i, row in keys.iterrows() :
    feature = {}
    feature["type"] = "Feature"
    feature["properties"] = {"name": row.keyword, "size": row.__getattr__("count") } #uso getattr, row.count mappa a una funzione
    feature["geometry"] = {"type":"Point", "coordinates": [row.x, row.y]}

    geojson["features"].append(feature)


with open(path+"keywords.geojson", "w") as f: 
    json.dump(geojson, f, indent = 2)