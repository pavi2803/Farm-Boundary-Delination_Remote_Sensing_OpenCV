#CANNY EDGE DETECTION ALGORITHM

import numpy as np
import cv2
import argparse
import os
from apya import raster
import matplotlib.pyplot as plt



#destination folder
sd_dir = '/home/pavithra/Desktop/New_test_folder/Canny_level2_outputs/'

#input image
image = '/home/pavithra/Desktop/Rasterimages/Test_pixel/T44QND_20190317T045659_B03_10m.tif'

#Reading the raster data
read_rast = raster.ReadRaster(image)
data_canni = read_rast.data

img = cv2.imread(image,cv2.IMREAD_UNCHANGED)
img = (img).astype(np.uint8)
print(type(img))

canny = cv2.Canny(img,100,200)

print(canny)



titles = ['Band-8', 'Output']

images = [img, (canny)]

#Dsiplaying original and canny transformed image

for i in range(2):
   plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.xticks([]), plt.yticks([])
plt.show()





#For saving in  GeoTiff format

sd_file = os.path.join(sd_dir, os.path.basename(image))
r_band_sd = raster.Raster(canny, extent=read_rast.extent, projection=read_rast.projection)
raster.WriteRaster(r_band_sd, sd_file)
print(sd_file)


#For Outline marking (Red)

fig, axes = plt.subplots(1, 2, figsize=(8, 8))
ax = axes.flatten()

ax[1].imshow(data_canni, cmap='gray')
ax[1].set_axis_off()
ax[1].contour(canny, [0.5], colors='r')
ax[1].set_title("Segmentation Output", fontsize=12)

ax[0].imshow(data_canni, cmap='gray')
ax[0].set_axis_off()
ax[0].set_title("17th March", fontsize = 12)

fig.tight_layout()
plt.show()




