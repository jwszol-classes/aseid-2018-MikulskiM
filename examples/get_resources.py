from podpac.datalib import terraintiles
from podpac.coordinates import Coordinates, clinspace
from podpac.datalib.terraintiles import TerrainTilesSource

from pyspark import SparkContext
import numpy as np

# sc = SparkContext(master="local[4]")

ZOOM_LEVEL = 9

# create coordinates for region
c = Coordinates([clinspace(75, -60, 1000), clinspace(-155, -35, 1000)], dims=['lat', 'lon'])

# get all tile urls for tile format ('geotiff') certain zoom level (9) within coordinates
tiles_urls = terraintiles.get_tile_urls('geotiff', ZOOM_LEVEL, coordinates=c)
tiles_urls = [tile.replace(f'geotiff/{ZOOM_LEVEL}/', '').replace('.tif', '') for tile in tiles_urls]

tiles_xy = [(int(tile.partition('/')[0]), int(tile.partition('/')[2])) for tile in tiles_urls]

# make query to get those resources


#https://s3.amazonaws.com/elevation-tiles-prod/geotiff/{z}/{x}/{y}.tif
# 'https://s3.amazonaws.com/elevation-tiles-prod/geotiff/{ZOOM_LEVEL}/{44}/{90}.tif'


# downloading single tile
node = TerrainTilesSource(source='s3://elevation-tiles-prod/geotiff/8/75/95.tif')
print(node.dataset.read(1)) # 2D matrix with height
# c = node.coordinates.transform('epsg:4326')
# output = node.eval(c)
