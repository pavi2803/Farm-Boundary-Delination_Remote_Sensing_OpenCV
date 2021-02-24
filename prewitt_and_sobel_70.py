#PREWITT AND SOBEL ALGORITHM

import cv2
import numpy as np
import argparse
import os
from apya import raster
import matplotlib.pyplot as plt

img = cv2.imread('/home/pavithra/Desktop/Rasterimages/Test_pixel/T44QND_20190317T045659_B03_10m.tif',cv2.IMREAD_UNCHANGED)
img = (img).astype(np.uint8)


#destination path
sd_dir = '/home/pavithra/Desktop/New_test_folder/Prewitt_outputs/'




#sobel
img_sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely



#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img, -1, kernely)
img_prewitt = img_prewittx + img_prewitty




titles = ['Band-4', 'Output']

#prewitt output
images = [img, (img_prewitt)]

#sobel output
#images = [img, (img_sobel)]



for i in range(2):
   plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.xticks([]), plt.yticks([])
plt.show()




#For saving in  GeoTiff format

sd_file = os.path.join(sd_dir, os.path.basename(image))
r_band_sd = raster.Raster(img_prewitt, extent=read_rast.extent, projection=read_rast.projection)
raster.WriteRaster(r_band_sd, sd_file)
print(sd_file)



