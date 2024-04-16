# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:25:09 2024

@author: kkeramati
"""

import spatialmath.base as smb
import numpy as np
import matplotlib.pyplot as plt

print(smb.rotx(0.2), "\n")
print(smb.rotx(30, "deg"), "\n")

R = smb.rotx(30, "deg")
print(np.linalg.det(R), "\n")

print(np.linalg.inv(R), "\n")
print(np.transpose(R), "\n")

print(smb.roty(0.2), "\n")
print(smb.rotz(0.3), "\n")

smb.trplot(smb.rotz(0.3))
plt.show()


ans = np.matmul(smb.rotx(np.pi / 2), smb.roty(np.pi / 2))
print(ans, "\n")

ans = np.matmul(smb.roty(np.pi / 2), smb.rotx(np.pi / 2))
print(ans, "\n")

print(smb.eul2r(0.1, 0.2, 0.3), "\n")
print(smb.tr2eul(smb.eul2r(0.1, 0.2, 0.3)), "\n")
print(smb.eul2r(0.1, -0.2, 0.3), "\n")
print(smb.tr2eul(smb.eul2r(0.1, -0.2, 0.3)), "\n")
ans = smb.tr2eul(smb.eul2r(0.1, -0.2, 0.3))
print(smb.eul2r(ans), "\n")
print(smb.rpy2r([0.3, 0.2, 0.1], order="xyz"), "\n")
