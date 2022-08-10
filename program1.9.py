import numpy as np

x = np.arange(16,dtype='int').reshape(-1,4)
print("Array :")
print(x)
print("\nNew array after swapping first and last rows of the said array:")
x = x[[-1,1,2,0]]
print(x)