import numpy as np

x = np.arange(16).reshape(4,4)
print("Array :")
print(x)

header = 'C1 C2 C3 C4'
np.savetxt('Array.txt',x,fmt="%d",header=header)

print("After loading, content of the text file:")
print(np.loadtxt('Array.txt'))
