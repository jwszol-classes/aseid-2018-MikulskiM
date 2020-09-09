import warnings
from podpac.datalib.terraintiles import TerrainTiles
from podpac import Coordinates, clinspace
import matplotlib.pyplot as plt

# Let's just ignore warnings
warnings.filterwarnings('ignore')

# create terrain tiles node
node = TerrainTiles(tile_format='geotiff', zoom=5)

# create coordinates to get tiles
# Coordinates for both americas in one: Coordinates([clinspace(75, -60, 1000), clinspace(-155, -35, 1000)], dims=['lat', 'lon'])
coords = Coordinates([clinspace(75, -60, 1000), clinspace(-155, -35, 1000)], dims=['lat', 'lon'])

# evaluate node
ev = node.eval(coords)

# print(ev)

# plot the evaluation
fig = plt.figure()
ev.plot(vmin=0, cmap='terrain')

# show plot
plt.show()

# input("waiting for enter or something")
