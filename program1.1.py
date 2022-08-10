import numpy as np

x = np.array([2,7,1,9,4,8])
y = np.array([9,4,6,2,9,6])
print("Array A")
print(x)
print("Array B")
print(y)
print("A>B")
print(np.greater(x,y))
print("A>=B")
print(np.greater_equal(x,y))
print("A<B")
print(np.less(x,y))
print("A<=B")
print(np.less_equal(x,y))

