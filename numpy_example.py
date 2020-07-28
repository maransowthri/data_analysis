import numpy as np
from matplotlib import pyplot as pp


np_arr = np.array([[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14 ], [15, 16,17, 18, 19, 20, 21]], dtype='int8')

# Properties

# print(np_arr)
# print(np_arr.ndim)
# print(np_arr.shape)
# print(np_arr.dtype)
# print(np_arr.itemsize)
# print(np_arr.nbytes)

# Accessing Elements
# print(np_arr[-1, -2])
# print(np_arr[:, 1])
# print(np_arr[0:3:2,0:8:3])
print(np_arr)
np_arr[1:, 2:6] = [[5, 5, 5, 5], [5, 5, 5, 5]]
print(np_arr)



# monalisa_np = np.loadtxt('monalisa.txt')
# print(monalisa_np.shape)
# print(monalisa_np.ndim)
# print(monalisa_np.dtype)
# print(pp.imshow(monalisa_np))

# mon_np = np.load('monalisa.npy')
# print(mon_np.shape)
# pp.imshow(mon_np)
# print(mon_np[1197, 803, 2])
# print(mon_np[-1, -1, -1])
# print(mon_np < 50)
# print(pp.imshow(mon_np))