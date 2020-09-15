import numpy as np
import matplotlib.pyplot as plt


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

mean_chunks = np.asarray([sum(sum(x))/CHUNK_SIZE**2 for x in chunks])
mean_chunks = mean_chunks.reshape(int(EDGE/CHUNK_SIZE), int(EDGE/CHUNK_SIZE))

result_lst = np.repeat(mean_chunks, CHUNK_SIZE, axis=0)
result_lst = np.repeat(result_lst, CHUNK_SIZE, axis=1)


plt.subplot(211)
plt.imshow(lst)
plt.subplot(212)
plt.imshow(result_lst)
plt.show()
