import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

from datetime import datetime
print(os.listdir('./'))

def interval_idx(ds, intervals):
	for idx, interval in enumerate(intervals):
		if ds in interval:
			return idx
	return -1

start_time = datetime.now()
filename = "gps_20161115_subset_500000"
gps = pd.read_csv("./" + filename,low_memory=False, 
				   dtype = {'vehicle_id': object, 'order_id':object, 'universal_time':np.int64, 'longitude':np.float32, 'latitude':np.float32})
# gps = pd.read_csv("./gps_20161115",
#                    names = ['vehicle_id', 'order_id', 'universal_time', 'longitude', 'latitude'],nrows = 100000)
print("read gps time : ", datetime.now() - start_time)

gps['mounth'] = gps.universal_time.apply(lambda x: int(datetime.utcfromtimestamp(x).strftime("%m")))
gps['day'] = gps.universal_time.apply(lambda x: int(datetime.utcfromtimestamp(x).strftime("%d")))
gps['hour'] = gps.universal_time.apply(lambda x: int(datetime.utcfromtimestamp(x).strftime("%H")))
gps['minute'] = gps.universal_time.apply(lambda x: int(datetime.utcfromtimestamp(x).strftime("%M")))
gps['second'] = gps.universal_time.apply(lambda x: int(datetime.utcfromtimestamp(x).strftime("%S")))
gps.drop(columns=["universal_time"])

max_longi = gps.longitude.max()
min_longi = gps.longitude.min()
max_lati = gps.latitude.max()
min_lati = gps.latitude.min()

ptr = [max_lati,max_longi]
ptl = [max_lati,min_longi]
pdr = [min_lati,max_longi]
pdl = [min_lati,min_longi]

print("Polygone in the map (lati,longi) :",[ptr, ptl, pdl, pdr])

# zone intervals
delta = 500

lati_intervals = pd.interval_range(start = min_lati, end = max_lati, periods = delta)
longi_intervals = pd.interval_range(start = min_longi, end = max_longi, periods = delta)

gps['lati_idx'] = gps.latitude.map(lambda x: interval_idx(x,lati_intervals))
gps['longi_idx'] = gps.longitude.map(lambda x: interval_idx(x,longi_intervals))

gps.to_csv("gps_20161115_with_zonelabels",index = False)

print("process gps-11-15 : ",datetime.now() - start_time)








