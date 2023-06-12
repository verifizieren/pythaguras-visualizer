import matplotlib.pyplot as plt
import numpy as np

# Coordinates
A = np.array([0, 0])
B = np.array([4, 0])
C = np.array([0, 3])

# Vectors AB, AC, and BC
AB = B - A
AC = C - A
BC = C - B

# Plot the triangle ABC
plt.figure()
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-')
plt.plot([A[0], C[0]], [A[1], C[1]], 'r-')
plt.plot([B[0], C[0]], [B[1], C[1]], 'g-')

# Annotate points
plt.text(A[0]-0.5, A[1], 'A')
plt.text(B[0], B[1]-0.5, 'B')
plt.text(C[0]-0.5, C[1], 'C')

# Display
plt.xlim(-1, 5)
plt.ylim(-1, 4)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Pythagorean Theorem: a² + b² = c²')
plt.grid()
plt.show()
