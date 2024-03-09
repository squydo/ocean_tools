from datetime import datetime, timedelta
import xarray as xr
import numpy as np

def seconds2date(seconds_since_2000):
    # Define what is zero in datetime space"
    zero_date = datetime(2000, 1, 1, 0, 0, 0)
    
    # Add the "ocean time" to the "zero date" in datetime space. "np.vectorize is so that 'timedelta' plays nice with xarry and Numpy array formats
    real_date = zero_date + np.vectorize(timedelta)(seconds=seconds_since_2000)

    return real_date

def ocean_time2date(ocean_time): #apply seconds_since_2000 function to ocean_time, converting into datetime space
    date_array = xr.apply_ufunc(seconds2date,ocean_time) 
    return date_array

def ocean_data2date(datafile): # load a file, isolate ocean_time, and then convert ocean_time to datetime space
    data = xr.open_dataset(datafile)
    ocean_time = data['ocean_time']
    date_array = xr.apply_ufunc(seconds2date,ocean_time)
    return date_array
