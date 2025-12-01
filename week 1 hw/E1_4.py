import numpy as np
import matplotlib.pyplot as plt


# inner product and norm calculations
vectors = [
    np.array([1, 0, 2]),
    np.array([3, 4]),
    np.array([-7, 2, -4, np.sqrt(12)])
]

for v in vectors:
    norm = np.linalg.norm(v)
    print(f"Vector {v} -> norm = {norm:.4f}")


# angle between two vectors
a = np.array([3, -2, 2])
b = np.array([1, 4, -1])

c = np.array([2, 0, 5, 1])
d = np.array([-1, 2, 0, 1])

inner_productA = np.dot(a, b)
cos_thetaA = inner_productA / (np.linalg.norm(a) * np.linalg.norm(b))
angle_degrees = np.degrees(np.arccos(cos_thetaA))
print(f"Angle between {a} and {b} -> {angle_degrees:.2f} degrees")

inner_productB = np.dot(c, d)
cos_thetaB = inner_productB / (np.linalg.norm(c) * np.linalg.norm(d))
angle_degreesB = np.degrees(np.arccos(cos_thetaB))
print(f"Angle between {c} and {d} -> {angle_degreesB:.2f} degrees")

#plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot vectors as arrows from origin
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='blue', arrow_length_ratio=0.1, linewidth=2, label='a')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='red', arrow_length_ratio=0.1, linewidth=2, label='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()

#orthogonal vector calculation