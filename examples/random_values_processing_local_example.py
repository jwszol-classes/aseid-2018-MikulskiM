import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def split(array, nrows, ncols):
    """Splits big matrix into array of submatrices (chunks)"""
    r, h = array.shape
    return array.reshape(h//nrows, nrows, -1, ncols).swapaxes(1, 2).reshape(-1, nrows, ncols)


TOTAL_ITEMS = 10000
EDGE = int(np.sqrt(TOTAL_ITEMS))
CHUNK_SIZE = 5
lst = np.random.randint(0, 10, TOTAL_ITEMS)\
        .reshape(EDGE, EDGE)

chunks = split(lst, CHUNK_SIZE, CHUNK_SIZE)

mean_chunks = np.asarray([np.mean(x) for x in chunks])
mean_chunks = mean_chunks.reshape(int(EDGE/CHUNK_SIZE), int(EDGE/CHUNK_SIZE))

result_lst = np.repeat(mean_chunks, CHUNK_SIZE, axis=0)
result_lst = np.repeat(result_lst, CHUNK_SIZE, axis=1)


max_val = np.max(result_lst)
min_val = np.min(result_lst)

print(f"max value: {max_val}, min value: {min_val}")

def ranges(start_val, stop_val, nb):
    step = (stop_val - start_val) / nb
    vals = [(start_val + step*i) for i in range(nb)]
    vals.append(stop_val)
    return vals


height_ranges = np.asarray(ranges(np.min(result_lst), np.max(result_lst), 6))
# from ranges -> to categories 1...6
result_lst = np.digitize(result_lst, bins=height_ranges, right=True)


print(result_lst)
plt.subplot(211)
plt.imshow(lst)
plt.subplot(212)
plt.imshow(result_lst)
plt.colorbar(ticks=range(0, 7))
plt.legend()
plt.show()
