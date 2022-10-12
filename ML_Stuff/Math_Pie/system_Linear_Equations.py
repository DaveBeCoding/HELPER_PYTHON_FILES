"""

8x + 3y - 2z = 9

-4x + 7y +5z = 15

3x + 4y - 12z = 35

"""

import numpy as np

A = np.array([[8, 3, -2], [-4, 7, 5], [3, 4, -12]])
b = np.array([9, 15, 35])
x = np.linalg.solve(A, b)

print(8*x[0] + 3*x[1] - 2*x[2])
print(-4*x[0] + 7*x[1] + 5*x[2])
print(3*x[0] + 4*x[1] - 12*x[2])
