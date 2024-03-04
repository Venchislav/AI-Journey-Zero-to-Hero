from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

vectors = np.array([[0, 0, 1, 1, 1, 1], [0, 0, 2, 2, 2, 2]]) 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for vector in vectors:
    v = np.array([vector[3],vector[4],vector[5]])
    vlength=np.linalg.norm(v)
    ax.quiver(vector[0],vector[1],vector[2],vector[3],vector[4],vector[5],
            pivot='tail',length=vlength,arrow_length_ratio=0.3/vlength)
ax.set_xlim([-4,4])
ax.set_ylim([-4,4])
ax.set_zlim([0,4])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()