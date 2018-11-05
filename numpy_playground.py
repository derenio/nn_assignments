import numpy as np


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
d = np.eye(2)
print(a, b, d, sep="\n")
print(a + b)
print(a * b)
print(a @ b)
print((a @ b) == [[1 * 5 + 2 * 7, 1 * 6 + 2 * 8], [3 * 5 + 4 * 7, 3 * 6 + 4 * 8]])
