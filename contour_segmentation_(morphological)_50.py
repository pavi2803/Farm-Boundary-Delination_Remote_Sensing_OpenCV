#Morphological Segmentation Algorithm - Usually works with identifying the variance in the pixel and marks a boundary over it. It works when the pixel values of the inside and outside regions of an object/farm have different averages.

import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float
from skimage.segmentation import (morphological_chan_vese,
                                  morphological_geodesic_active_contour,
                                  inverse_gaussian_gradient,
                                  checkerboard_level_set,
                                  circle_level_set)

import glob
from scipy import ndimage
import numpy as np
import os

from apya import raster
from PIL import Image


#function which iterates the process and stores the markings

def store_evolution_in(lst):
    """Returns a callback function to store the evolution of the level sets in
    the given list.
    """

    def _store(x):
        lst.append(np.copy(x))

    return _store



in_dir = "/home/pavithra/Desktop/Satyukt/20th Dec 2018_B2.tif"
sd_dir = "/home/pavithra/Desktop/New_test_folder"


r_band = raster.ReadRaster(in_dir)
#data = r_band.data

image = r_band.data


init_ls = checkerboard_level_set(image.shape, 5)

evolution = []
callback = store_evolution_in(evolution)
ls = morphological_chan_vese(image, 100, init_level_set=init_ls, smoothing=5,
                             iter_callback=callback)

fig, axes = plt.subplots(1, 2, figsize=(8, 8))
ax = axes.flatten()

ax[1].imshow(image, cmap='gray')
ax[1].set_axis_off()
ax[1].contour(ls, [0.5], colors='r')
ax[1].set_title("Segmentation Output", fontsize=12)

ax[0].imshow(image, cmap='gray')
ax[0].set_axis_off()
ax[0].set_title("20th Dec 2019 Band_2", fontsize = 12)



plt.hist(ls)
fig.tight_layout()
plt.show()









