#This program deals with preprocessing the bands firstly by using SD, then by applying the Guassian filter to remove noises, and then adding the contrast to improve visiblity of details in the bands. After the Guassian filter, the contrast feature is applied over the bands, because the guassian filter usually removes the noise, but reduces the contrast.

import glob
from scipy import ndimage
import numpy as np
import os
from apya import raster
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering
import scipy
from apya import raster
from scipy import misc
from scipy.cluster.vq import kmeans,vq,whiten
from skimage import filters
from skimage import measure

#finding the Standard deviation of the bands
#For cloudy data, the 'less cloudy' data is applied feature extraction

in_dir = "/home/pavithra/Desktop/Rasterimages/NEW_MEX_DATA/mex_data/B12/*.tif"
in_files = glob.glob(in_dir)
in_files.sort()
sd_dir = "/home/pavithra/Desktop/Rasterimages/NEW_SD/SD_B12"

for in_file in in_files:
    r_band = raster.ReadRaster(in_file)
    data = r_band.data

    out_sd = ndimage.generic_filter(data, np.var, size=3)**0.5


    sd_file = os.path.join(sd_dir, os.path.basename(in_file))

    r_band_sd = raster.Raster(out_sd, extent=r_band.extent, projection=r_band.projection)

    raster.WriteRaster(r_band_sd, sd_file)

    print(sd_file)


#Applying Guassian filter

in_dirtwo = "/home/pavithra/Desktop/Rasterimages/NEW_SD/SD_B12/*.tif"
in_filestwo = glob.glob(in_dirtwo)
in_filestwo.sort()
sd_dirtwo = "/home/pavithra/Desktop/Rasterimages/NEW_Sharpened_data/B12"

for in_file in in_filestwo:
    r_bandtwo = raster.ReadRaster(in_file)
    datatwo = r_bandtwo.data

    blurred_f = ndimage.gaussian_filter(datatwo, 2)
    filter_blurred_f = ndimage.gaussian_filter(blurred_f, 1)
    alpha = 30
    sharpened = blurred_f + alpha * (blurred_f - filter_blurred_f)


    sd_filetwo = os.path.join(sd_dirtwo, os.path.basename(in_file))

    r_band_sdtwo = raster.Raster(sharpened, extent=r_bandtwo.extent, projection=r_bandtwo.projection)

    raster.WriteRaster(r_band_sdtwo, sd_filetwo)

    print(sd_filetwo)



#Adding contrast to the guassian filter images

in_dirthree = "/home/pavithra/Desktop/Rasterimages/NEW_Sharpened_data/B12/*.tif"
in_filesthree = glob.glob(in_dirthree)
in_filesthree.sort()
sd_dirthree = "/home/pavithra/Desktop/Rasterimages/NEW_Feature_data/B12"




for in_file in in_filesthree:
    r_bandthree = raster.ReadRaster(in_file)
    datathree = r_bandthree.data


    minval = np.percentile(datathree, 2)
    maxval = np.percentile(datathree, 98)
    datathree = np.clip(datathree, minval, maxval)
    datathree = ((datathree - minval) / (maxval - minval)) * 255
    Image.fromarray(datathree.astype(np.uint8))

   

    sd_filethree = os.path.join(sd_dirthree, os.path.basename(in_file))

    r_band_sdthree = raster.Raster(datathree, extent=r_bandthree.extent, projection=r_bandthree.projection)

    raster.WriteRaster(r_band_sdthree, sd_filethree)

    print(sd_filethree)

















