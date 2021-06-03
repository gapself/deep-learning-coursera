import numpy as np

a = np.random.rand(5)
print(a)
print(a.shape)
print(a.T)
print(a == a.T)
print(np.dot(a, a.T))  # num

# better practice:
a = np.random.rand(5, 1)
print(a)
print(a.shape)
print(a.T)
print(np.dot(a, a.T))  # matrix
