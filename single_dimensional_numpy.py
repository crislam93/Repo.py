import numpy as np

#Single-Dimensional Array
a = np.array([1,2,3])

#Multi-Dimensional Array
b = np.array([(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,1)])

print("{} (Rows, Columns) = {}".format(b, b.shape))
print("Dimensions = {}".format(b.ndim))

print(a.max(), a.min()) #máximo y mínimo valor
print(a.sum()) #suma 
print(b.sum())