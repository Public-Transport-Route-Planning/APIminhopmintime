#%%
from folium import plugins
import folium
import pandas as pd
import numpy as np
import random



start_lat = 13.751797798437075
start_lon = 100.50820436717605
dest_lat =  13.761184103576973
dest_lon = 100.6456136401535

parsed_data, route_ansLines = getRoute(start_lat, start_lon, dest_lat, dest_lon)

bus_path = 'data/csv/bus_routes.csv'
bus_route = pd.read_csv(bus_path)
line = bus_route[bus_route["route_id"] == "169"]["polyline"].iloc[0]
rpath = eval(line)


#%%
f = folium.Figure(width=800, height=400)
m = folium.Map(
    width='100%',
    height='100%',
    tiles="cartodbpositron",
    location=(13.798969,100.548561),
    zoom_start=17
).add_to(f)

for route_id, ansLines in route_ansLines.items():
    color = "#" + "%06x" % random.randint(0, 0xFFFFFF)
    folium.PolyLine(ansLines, color=color, weight=5, opacity=0.5,popup=route_id).add_to(m)


