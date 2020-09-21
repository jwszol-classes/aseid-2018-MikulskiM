import warnings
from podpac.datalib.terraintiles import TerrainTiles
from podpac import Coordinates, clinspace
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
import matplotlib as mpl
import argparse
from timeit import default_timer as timer

# Let's just ignore warnings
warnings.filterwarnings('ignore')


def split(array, nrows, ncols):
    """Splits big matrix into array of submatrices (chunks)"""
    r, h = array.shape
    return array.reshape(h//nrows, nrows, -1, ncols).swapaxes(1, 2).reshape(-1, nrows, ncols)


def ranges(start_val, stop_val, nb):
    step = (stop_val - start_val) / nb
    vals = [(start_val + step * i) for i in range(1, nb + 1)]
    vals.insert(0, 1)
    vals.insert(0, 0)
    print(vals)

    def my_round(val):
        return float("{:.2f}".format(val))

    height_labels = [f'{i} - [{my_round(vals[i])} : {my_round(vals[i + 1])}]' for i in range(len(vals) - 1)]
    print(height_labels)
    return vals, height_labels

def get_terrain_tiles(which):
    # create coordinates to get tiles
    node = TerrainTiles(tile_format='geotiff', zoom=5)
    coords = 0
    if (which == 'both'):
        coords = Coordinates([clinspace(75, -60, 1000), clinspace(-155, -35, 1000)], dims=['lat', 'lon'])
    elif(which == 'north'):
        coords = Coordinates([clinspace(75, 10, 1000), clinspace(-155, -50, 1000)], dims=['lat', 'lon'])
    elif(which == 'south'):
        coords = Coordinates([clinspace(15, -60, 1000), clinspace(-85, -45, 1000)], dims=['lat', 'lon'])
    # evaluate node
    ev = node.eval(coords)
    data = np.asarray(ev.data)

    return data

def process_terrain_tiles(data, CHUNK_SIZE, EDGE):
    chunks = split(data, CHUNK_SIZE, CHUNK_SIZE)

    mean_chunks = np.asarray([np.max(x) - np.min(x) for x in chunks])
    mean_chunks = mean_chunks.reshape(int(EDGE / CHUNK_SIZE), int(EDGE / CHUNK_SIZE))

    result_lst = np.repeat(mean_chunks, CHUNK_SIZE, axis=0)
    result_lst = np.repeat(result_lst, CHUNK_SIZE, axis=1)

    return result_lst

def discretize_terrain_tiles(data):
    height_ranges, height_labels = ranges(np.min(data), np.max(data), 6)
    height_ranges = np.asarray(height_ranges)

    # from ranges -> to categories 1...6
    data = np.digitize(data, bins=height_ranges, right=True)
    print(height_ranges)
    return data, height_labels


def main():

    parser = argparse.ArgumentParser(description='Process North, South or Both Americas at once')
    parser.add_argument("--waterzero", default=True, help="Decide, if values below sea level should be equal 0")
    parser.add_argument('--area', choices=['both', 'north', 'south', 'latin'], default='both',
                        help='decide which area should be processed')

    args = parser.parse_args()
    print(args)

    TOTAL_ITEMS = 1000 * 1000
    EDGE = int(np.sqrt(TOTAL_ITEMS))
    CHUNK_SIZE = 5

    start_downloading = timer()
    data_np = get_terrain_tiles(args.area)
    end_downloading = timer()
    download_time = end_downloading - start_downloading

    start_processing = timer()
    data_to_process = deepcopy(data_np)
    data_to_process = np.clip(data_to_process, 0, np.max(data_to_process))

    result_lst = process_terrain_tiles(data_to_process, CHUNK_SIZE, EDGE)
    result_lst, height_labels = discretize_terrain_tiles(result_lst)
    end_processing = timer()
    processing_time = end_processing - start_processing

    print(f'Downloading time: {download_time} \n Processing time: {processing_time}')
    plt.subplot(211)
    plt.imshow(data_np)

    plt.subplot(212)

    #discretize colorbar
    cmap = mpl.cm.viridis
    bounds = list(range(0, 8))
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    plt.imshow(result_lst, norm=norm)
    cbar = plt.colorbar()
    cbar.set_ticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
    cbar.set_ticklabels([0, 1, 2, 3, 4, 5, 6])
    cbar.set_ticklabels(height_labels)
    plt.show()


if __name__ == '__main__':
    main()
