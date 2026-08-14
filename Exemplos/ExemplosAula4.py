import numpy as np

arr = np.array([1, 2, 3])
print(arr)
print(type(arr))
print(arr.size)

print(" ")

mtz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mtz)
print(mtz.shape)

print(" ")

mtz = np.arange(2, 31, 4)
print(mtz)
print(mtz.reshape(2, 4))

print(" ")

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([60, 70, 80, 90, 100])

print(arr1.sum(), arr1.mean())

print(" ")

arr = np.random.randint(1,26, [5,5])
print(arr)



