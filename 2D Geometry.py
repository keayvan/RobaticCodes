# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:20:11 2024

@author: kkeramati
"""

import spatialmath.base as smb
import numpy as np
from matplotlib import pyplot as plt

### Describing rotation in 2D###
##What to learn here:
    #1. 2D rotation matris
    #2. Det calculation
    #3. inverse matris
    #4. transpose matris
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

###Describing rotation and translation in 2D###

# print(smb.transl2(1, 2), "\n")
# print(smb.rot2(30, "deg"), "\n")
# print(smb.trot2(30, "deg"), "\n")
# print(np.matmul(smb.transl2(1, 2), smb.trot2(30, "deg")), "\n")
# print(smb.trot2(30, "deg", t=[1, 2]), "\n")


def point_new_cordinate2D(Point,
                        rotation=30,
                        translation = [1,2],
                        ):

    T1 = smb.trot2(rotation, "deg", t=translation)
    P = np.asarray([[Point[0]], [Point[1]],[1]])
    P1 = np.matmul(np.linalg.inv(T1),P)
    return P1, T1

P1, T1 = point_new_cordinate2D(Point = [3,2])
smb.trplot2(T1)
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.show()
P= [3,2]
# print(P, "\n")

plt.plot(P[0], P[1], "b*")
plt.show()

# print(P1)

def point_new_cord_to_ref_cord(p_cord_new_frame,
                               rot_new_frame,
                               trans_new_frame):
    T1 = smb.trot2(rot_new_frame, "deg", t = trans_new_frame)
    P = np.asanyarray([[p_cord_new_frame[0]],[p_cord_new_frame[1]],[1]])
    P1= np.matmul(T1,P)
    return P1, T1

P2, T2 = point_new_cord_to_ref_cord(p_cord_new_frame=[1,2],
                               rot_new_frame= 60,
                               trans_new_frame=[3,4])

print(P2)