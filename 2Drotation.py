# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:20:11 2024

@author: kkeramati
"""

import spatialmath.base as smb
import numpy as np
from matplotlib import pyplot as plt

# print(smb.rot2(0), "\n")
# print(smb.rot2(0.2), "\n")

# R = smb.rot2(30,"deg")
# print(R, "\n")

# c1 = R[:, 0]
# c2 = R[:, 1]

# print(np.dot(c1, c2), "\n")
# print(np.linalg.det(R), "\n")
# print(np.linalg.inv(R), "\n")
# print(np.transpose(R), "\n")


# smb.trplot2(R)
# plt.xlim(-1, 1.5)
# plt.ylim(-1, 1.5)
# plt.show()

print(smb.transl2(1, 2), "\n")
print(smb.rot2(30, "deg"), "\n")
print(smb.trot2(30, "deg"), "\n")
print(np.matmul(smb.transl2(1, 2), smb.trot2(30, "deg")), "\n")
print(smb.trot2(30, "deg", t=[1, 2]), "\n")

T1 = smb.trot2(30, "deg", t=[1, 2])
smb.trplot2(T1)
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.show()


P = np.asarray([[3], [2]])

print(P, "\n")

plt.plot(P[0], P[1], "b*")
plt.show()

P1 = np.matmul(np.linalg.inv(T1), [[3], [2], [1]])
print(P1)
