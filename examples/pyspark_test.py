from pyspark import SparkContext
import numpy as np

sc = SparkContext(master="local[4]")
lst = np.random.randint(0, 10, 20)
A = sc.parallelize(lst)
print(A.collect())
print(type(A))


