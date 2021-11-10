# Code from https://www.youtube.com/watch?v=C70k_K19ls8&t=13s

import numpy as np
import matplotlib.pyplot as plt

# Try the following values:
# multiplier 30 and no_points from 144 to 149
# See https://www.geogebra.org/m/dqKkQEv7
multiplier = 30
no_points = 144

mult_list = []
mod_list = []
theta = 360 / no_points
points = []
p1 = [0, 1]
circle = plt.Circle((0, 0), 1, color='r', fill=False, linewidth=0.05)
fig, ax = plt.subplots()
ax.add_artist(circle)


def transformation(point, angle, list1):
    a = [np.cos(np.radians(angle)), np.sin(np.radians(angle))]
    b = [-np.sin(np.radians(angle)), np.cos(np.radians(angle))]
    matrix = [a, b]
    point2 = list(np.dot(matrix, point))
    list1.append(point2)

i = 0
while i < no_points:
    transformation(p1, theta * i, points)
    i += 1

num_list = [i for i in range(0, no_points)]  # position of points on circle

for i in num_list:
    s = multiplier * i
    mult_list.append(s)  # multiplying position of points by the multiplier

mod_sums = [s % no_points for s in mult_list]
points2 = []

for i in mod_sums:
    s = points[i]
    points2.append(s)

plt.axis("equal")
plt.axis('off')
x = []
y = []
c = []
z = []

for i in points:
    x.append(i[0])
    y.append(i[1])

for i in points2:
    c.append(i[0])
    z.append(i[1])

i = 0
while i < len(x):
    plt.plot([x[i], c[i]], [y[i], z[i]], 'r-', linewidth=0.3)
    i += 1

plt.show()
