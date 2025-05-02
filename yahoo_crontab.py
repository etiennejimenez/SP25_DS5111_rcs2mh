import os
from datetime import datetime
storage_path = '/home/ubuntu/SP25_DS5111_rcs2mh/collected_data/'
current_time = datetime.fromtimestamp(datetime.now().timestamp())
current_time = str(current_time)[:-7]
filename = "ygainers" + current_time + ".csv"
filename = filename.replace(' ','_')
os.rename('ygainers_norm.csv', storage_path + filename)
