import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import random
from datetime import datetime

def subsample(num, filename = "gps_20161115"):
	gps = pd.read_csv("./"+filename,
					names = ['vehicle_id', 'order_id', 'universal_time', 'longitude', 'latitude'])
	
	gps.sample(n = num).to_csv("gps_20161115_subset_"+str(num),index = False)


print(os.listdir("./"))

start = datetime.now()

num = 500000
subsample(num)

print("subsample num = ", num, " time consum: ", datetime.now()-start)