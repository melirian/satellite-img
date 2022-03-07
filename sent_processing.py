from glob import glob
import os

import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

import rasterio as rio

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

import plotly.graph_objects as go

np.seterr(divide='ignore', invalid='ignore')

def sentinel_read():
    bands = glob('/content/gdrive/MyDrive/sentinel/2017-06-20/S2A_MSIL1C_20170620T082011_N0205_R121_T34JEP_20170620T084200.SAFE/GRANULE/L1C_T34JEP_A010414_20170620T084200/IMG_DATA/*.jp2')

    # Read band metadata and arrays
    bands.sort()
    l = []

    for i in bands:
      with rio.open(i, 'r') as f:
        l.append(f.read(1))
    return l

bands = sentinel_read()
