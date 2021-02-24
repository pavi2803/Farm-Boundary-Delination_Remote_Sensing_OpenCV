import glob
from scipy import ndimage
import numpy as np
import cv2
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
import filecmp
import math


in_dir = "/home/pavithra/Desktop/Rasterimages/AndhraPradesh_Data/Cloudy/*_SCL_20m.tif"
in_files = glob.glob(in_dir)
in_files.sort()

sd_dir = "/home/pavithra/Desktop/Rasterimages/AndhraPradesh_Data/*.tif"
sd_files = glob.glob(sd_dir)
sd_files.sort()


sd_datacc = "/home/pavithra/Desktop/Rasterimages/AndhraPradesh_Data/Data_cc/"


for in_file in in_files:
    for ik_file in sd_files:
        one = os.path.basename(in_file)
        on = one.rsplit('_',2)
        two = os.path.basename(ik_file)
        tw = two.rsplit('_',2)
        if(on[0] == tw[0]):
           r_band = raster.ReadRaster(ik_file)
           data = r_band.data
           #data1 = r_band.astype(np.uint8)
           for i in range(len(data)):
               for j in range(len(data[0])):
                   if(data[i,j]>3000):
                      data[i,j] = np.nan
                   else:
                      data[i,j] = data[i,j]
          
           sd_file = os.path.join(sd_datacc, os.path.basename(ik_file))
           r_band_cc = raster.Raster(data, extent=r_band.extent, projection=r_band.projection)
           raster.WriteRaster(r_band_cc, sd_file)
           print(sd_file)                          
        else:
           print('file not matched')
    







