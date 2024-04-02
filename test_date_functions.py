from date_functions import *
from datetime import datetime, timedelta
import xarray as xr
import numpy as np

##########################
# Demo of ocean_data2date

time = ocean_data2date('C:\\Users\\sydjw\\Documents\\[C]Worthy\\Iceland3_rnd.20120516130000_sh.nc')
print(time)

##########################
# Demo of ocean_time2date

# data = xr.open_dataset('C:\\Users\\sydjw\\Documents\\[C]Worthy\\Iceland3_rnd.20120516130000_sh.nc')
# ocean_time = data['ocean_time']
# time = ocean_time2date(ocean_time)
# print(time)

###########################




