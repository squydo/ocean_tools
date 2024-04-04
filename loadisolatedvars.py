import xarray as xr

def loadisolatedvars(file_path, *variables)
    
    variable_list = [var for var in variables]

    ds = xr.open_mfdataset(
        file_path, #path to file folder with /*.nc
        combine='nested', # combination instruction
        concat_dim=["time"], #concatination instruction
        preprocess=preprocess, #isolate DIC and Alk variables by invoking the preprocess function
        chunks={}, #allow vars
        parallel=True #induce paralell processing 
    )
    return ds

def preprocess(x)
    return x[variable_list]




    