from folium.plugins import HeatMap,HeatMapWithTime
import folium
import pandas as pd 
import numpy as np


def heatmap(gps):
	veh_sum = gps.vehicle_id.value_counts()
	veh_sum = veh_sum[veh_sum<5].index

	veh_array = gps[gps.vehicle_id.isin(veh_sum)][["latitude","longitude"]].values.tolist()
	
	m = folium.Map(location = [30.72775, 104.12957])
	m.add_child(HeatMap(veh_array,radius=5, gradient={.4: 'blue', .65: 'lime', 1: 'yellow'}))
	m.save("heatmap.html")
	return m
	
def heatmap_time(gpslabel):
	
	heat_data = []
	for hour in range(24):
		gps_data = gpslabel[gpslabel.hour == hour][["latitude","longitude","hour"]].values.tolist()
		heat_data.append(gps_data)
		
	m = folium.Map(location = [30.72775, 104.12957])	
	HeatMapWithTime(data = heat_data,radius=5, gradient={.4: 'blue', .65: 'lime', 1: 'yellow'}).add_to(m)
	m.save("heatmap_time.html")
	return m

gps = pd.read_csv("./gps_20161115_with_zonelabels")

heatmap(gps)
heatmap_time(gps)