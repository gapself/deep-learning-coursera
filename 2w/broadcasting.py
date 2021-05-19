import numpy as np

fruits = ['apples', 'beef', 'eggs', 'potatoes']
carb = [56.0, 0.0, 4.4, 68.0]
protein = [1.2, 104.0, 52.0, 8.0]
fat = [1.8, 135.0, 99.0, 0.9]

A = np.array([carb, protein, fat])
print(A)
print(A.shape)

cal = A.sum(axis=0)  # axis=0 means sum up vertically
print(cal)
print(cal.shape)

percentage = 100 * A / cal.reshape(1, 4)  # .reshape(1,4) optional, good practice
print(percentage)