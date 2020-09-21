import warnings
from podpac.datalib.terraintiles import TerrainTiles
from podpac import Coordinates, clinspace
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
import matplotlib as mpl

# Let's just ignore warnings
warnings.filterwarnings('ignore')

# force matplotlib not to use any Xwindows backend
mpl.use('Agg')

def split(array, nrows, ncols):
    """Splits big matrix into array of submatrices (chunks)"""
    r, h = array.shape
    return array.reshape(h//nrows, nrows, -1, ncols).swapaxes(1, 2).reshape(-1, nrows, ncols)


def ranges(start_val, stop_val, nb):
    step = (stop_val - start_val) / nb
    vals = [(start_val + step*i) for i in range(nb)]
    vals.append(stop_val)
    return vals


TOTAL_ITEMS = 1000 * 1000
EDGE = int(np.sqrt(TOTAL_ITEMS))
CHUNK_SIZE = 5

# create terrain tiles node
node = TerrainTiles(tile_format='geotiff', zoom=5)

# create coordinates to get tiles
coords = Coordinates([clinspace(75, 10, 1000), clinspace(-155, -50, 1000)], dims=['lat', 'lon'])

# evaluate node
ev = node.eval(coords)

data_np = np.asarray(ev.data)
data_to_process = deepcopy(data_np)

chunks = split(data_to_process, CHUNK_SIZE, CHUNK_SIZE)

mean_chunks = np.asarray([np.max(x)-np.min(x) for x in chunks])
mean_chunks = mean_chunks.reshape(int(EDGE/CHUNK_SIZE), int(EDGE/CHUNK_SIZE))

result_lst = np.repeat(mean_chunks, CHUNK_SIZE, axis=0)
result_lst = np.repeat(result_lst, CHUNK_SIZE, axis=1)

height_ranges = np.asarray(ranges(np.min(result_lst), np.max(result_lst), 6))
# from ranges -> to categories 1...6
result_lst = np.digitize(result_lst, bins=height_ranges, right=True)


plt.subplot(211)
plt.imshow(data_np)

plt.subplot(212)

# discrete legend
cmap = mpl.cm.viridis
bounds = list(range(1, 8))
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

plt.imshow(result_lst, norm=norm)

# align labels between ticks
cbar = plt.colorbar()
cbar.set_ticks([1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
cbar.set_ticklabels([1, 2, 3, 4, 5, 6])

# saving results to .png file
plt.savefig('result.png')

plt.show()


