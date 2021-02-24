import glob
from scipy import ndimage
import numpy as np
import os

from apya import raster

in_dir = "/home/tomer/Projects/1000/algos/farm_boundaries_s2/example/s2_data/*.tif"
in_files = glob.glob(in_dir)
in_files.sort()

sd_dir = "/home/tomer/Projects/1000/algos/farm_boundaries_s2/example/sd"

for in_file in in_files:
    r_band = raster.ReadRaster(in_file)
    data = r_band.data

    out_sd = ndimage.generic_filter(data, np.var, size=3)**0.5

    sd_file = os.path.join(sd_dir, os.path.basename(in_file))

    r_band_sd = raster.Raster(out_sd, extent=r_band.extent, projection=r_band.projection)

    raster.WriteRaster(r_band_sd, sd_file)

    print(sd_file)

