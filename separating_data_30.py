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


#The images are separated based on the percentage of NA precent. Into less and more cloudy category.

in_dir = "/home/pavithra/Desktop/Rasterimages/AndhraPradesh_Data/Data_cc/*.tif"
in_files = glob.glob(in_dir)
in_files.sort()

sd_one = "/home/pavithra/Desktop/Rasterimages/Less_cloud/"
sd_two = "/home/pavithra/Desktop/Rasterimages/More_cloud/"

for in_file in in_files:
    r_band = raster.ReadRaster(in_file)
    data = r_band.data
    null = np.count_nonzero(np.isnan(data))
    nonnull = np.count_nonzero(~np.isnan(data))

    val = (null / (null+nonnull))*100

    if(val < 50):
       sd_file = os.path.join(sd_one, os.path.basename(in_file))
       
       raster.WriteRaster(r_band, sd_file)
       print(sd_file)

    else:
       
       sd_file = os.path.join(sd_two, os.path.basename(in_file))

       raster.WriteRaster(r_band, sd_file)
       print(sd_file)
       

           



        

