import numpy as np

x =  np.array([2,2,3,2,1])
y =  np.array([2,3,4,3,1])

print("Original Arrays : ")
print(x)
print(y)

print("\nTest said two arrays are equal (element wise) or not:?")
print(x==y)
print(np.equal(x,y))
