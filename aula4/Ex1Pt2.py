import numpy as np

arr1 = np.arange(0, 51, 2)
arr2 = np.arange(50, 101, 2)

arr3 = np.concatenate((arr1, arr2))
arr3 = np.sort(arr3)

print(arr3)