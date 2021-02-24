#CLOUDY/CLEAR DATA CLASSIFICATION

#The constitution of the percentage of the pixel values in the SCL data, paves a way for making a classification.
#The Values of 3-5 are considered as the non cloudy data. Values of 6,7 or anything upto 11 are considered cloudy.
#The Valid range of SCL values are 0-11


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

in_dir = "/home/pavithra/Desktop/Rasterimages/AndhraPradesh_SCL/*SCL_20m.tif"


in_files = glob.glob(in_dir)
in_files.sort()


sd_dir = "/home/pavithra/Desktop/Rasterimages/AndhraPradesh_Data/Cloudy/"
sd_dir2 = "/home/pavithra/Desktop/Rasterimages/AndhraPradesh_Data/clear_data/"


for in_file in in_files:
  reading = raster.ReadRaster(in_file)
  im = Image.open(in_file,'r')
  pix_val = list(im.getdata())

  #getting the count of values
  five = pix_val.count(5.0)
  seven = pix_val.count(7.0)
  four = pix_val.count(4.0)
  three = pix_val.count(3.0)

  #print('5',five)
  #print('7',seven)
  #print('4',four)
  #print('3',three)

  #total pixel count  
  total = len(pix_val)

  #Percentage of each value
  a = (five*100/total)
  b = (seven*100/total)
  c = (four*100/total)
  d= (three*100/total)
  if(a+c == 100 or a+c == 99):
    print("Good")



  if((a>c>d>b or a>d>c>b)):
    sd_file = os.path.join(sd_dir2, os.path.basename(in_file))
    raster.WriteRaster(reading, sd_file)
    print(sd_file)
  elif(c>a>d>b or c>d>a>b):
    sd_file = os.path.join(sd_dir2, os.path.basename(in_file))
    raster.WriteRaster(reading, sd_file)
    print(sd_file)
  elif(d>a>c>b or d>c>a>b):
    sd_file = os.path.join(sd_dir2, os.path.basename(in_file))
    raster.WriteRaster(reading, sd_file)
    print(sd_file)

  elif(c>b>a):
    sd_file = os.path.join(sd_dir2, os.path.basename(in_file))
    raster.WriteRaster(reading, sd_file)
    print(sd_file)
  elif(a>b>c):
    sd_file = os.path.join(sd_dir2, os.path.basename(in_file))
    raster.WriteRaster(reading, sd_file)
    print(sd_file)
   
  elif(a+b+c==0):
    sd_file = os.path.join(sd_dir2, os.path.basename(in_file))
    raster.WriteRaster(reading, sd_file)
    print(sd_file)

#Images having a dominating percentage of '7' value are put into as cloudy 
  else:
    sd_files = os.path.join(sd_dir, os.path.basename(in_file))
    raster.WriteRaster(reading, sd_files)
    print(sd_files)





