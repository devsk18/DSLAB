import numpy as np

x = np.array([[2,5],[6,8]])
print("Array :")
print(x)

print("Sum of elements in the array")
print(np.sum(x))

print("Sum of elements in each column")
print(np.sum(x, axis=0))

print("Sum of elements in each row")
print(np.sum(x, axis=1))

