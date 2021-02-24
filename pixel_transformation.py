#This program coverts the featured images into a different pixel composition. Replacing the black and grey ones with white and the white with black, to make the boundaries more clear, to implement the algorithm.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import ndimage as ndi
import cv2
from skimage.feature import shape_index
from apya import raster
from PIL import Image
import os
import cv2


im = raster.ReadRaster('/home/pavithra/Desktop/Rasterimages/NEW_Feature_data/B02/T14QQF_20181220T165719_B02_10m.tif')

sd_dir = "/home/pavithra/Desktop/Satyukt"

data = im.data


print(data[1][2])

print(data.shape)

#955 is the number of pixels in row and 1190 in the column

for i in range(0,955):
  for j in range(0,1190):
    if(data[i][j] <= 65):
       data[i][j] = 255
    else:
       data[i][j] = 0


print(data)


sd_file = os.path.join(sd_dir, os.path.basename('20th Dec 2018_B2.tif'))

r_band_sd = raster.Raster(data, extent=im.extent, projection=im.projection)

raster.WriteRaster(r_band_sd, sd_file)
print(sd_file)





