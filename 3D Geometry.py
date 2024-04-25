# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:25:09 2024

@author: kkeramati
"""

import spatialmath.base as smb
import numpy as np
import matplotlib.pyplot as plt

###Describing rotation in 3D###

# print(smb.rotx(0.2), "\n")
# print(smb.rotx(30, "deg"), "\n")

# R = smb.rotx(30, "deg")
# # print(np.linalg.det(R), "\n")

# print(np.linalg.inv(R), "\n")
# print(np.transpose(R), "\n")

# print(smb.roty(0.2), "\n")
# print(smb.rotz(0.3), "\n")

# smb.trplot(smb.rotz(0.3))
# plt.show()


# ans = np.matmul(smb.rotx(np.pi / 2), smb.roty(np.pi / 2))
# print(ans, "\n")

# ans = np.matmul(smb.roty(np.pi / 2), smb.rotx(np.pi / 2))
# print(ans, "\n")

# print(smb.eul2r(0.1, 0.2, 0.3), "\n")
# print(smb.tr2eul(smb.eul2r(0.1, 0.2, 0.3)), "\n")
# print(smb.eul2r(0.1, -0.2, 0.3), "\n")
# print(smb.tr2eul(smb.eul2r(0.1, -0.2, 0.3)), "\n")
# ans = smb.tr2eul(smb.eul2r(0.1, -0.2, 0.3))
# print(smb.eul2r(ans), "\n")
# print(smb.rpy2r([0.3, 0.2, 0.1], order="xyz"), "\n")

# R = smb.eul2r(0.1, 0.2, 0.3)
# print(R, "\n")
# smb.trplot(R)
# plt.show()
# print(np.linalg.eig(R)[0], "\n")
# e, v = np.linalg.eig(R)
# print(v, "\n")
# print(e, "\n")

# print(smb.tr2angvec(R), "\n")
# th, v = smb.tr2angvec(R)
# print(th, "\n")
# print(v, "\n")

# print(smb.angvec2r(th, v), "\n")
# R = smb.eul2r(0.1,0.2,0.3)
# smb.trplot(R)
# plt.show()
# e , v = np.linalg.eig(R) #Eigenvalue and eigenvector
# th , v = smb.tr2angvec(R) #Calculate the rotation axis and rotation angel
# R = smb.eul2r(0.1, 0.2, 0.3)
# q = smb.r2q(R)
# q_rev = smb.qconj(q)  #Reverse of the q

# smb.qprint(smb.qqmul(q,q_rev))
##Quaternions representation of the rotation in 3D

#Hamiltonian product definition

def qqdiv(q1,q2):
    q1 = smb.getvector(q1,4)
    q2 = smb.getvector(q2,4)
    
    s1 = q1[0]
    v1 = q1[1:4]
    
    s2 = q2[0]
    v2 = q2[1:4]
    
    quat =np.zeros(4)
    quat[0] = s1*s2 +np.dot(v1,v2)
    quat[1:4] = s1*v2 - s2*v1+ np.cross(v1,v2)
    return quat

R = smb.eul2r(0.1, 0.2, 0.3)
print(R, "\n")
smb.qprint(smb.r2q(R))
print("\n")
q = smb.r2q(R)
smb.qprint(q)
print("\n")
smb.trplot(R)

smb.qprint(smb.qconj(q)) #inverse of the Quaternion
print("\n")

smb.qprint(smb.qqmul(q, smb.qconj(q)))
print("\n")

smb.qprint(qqdiv(q, q))
print("\n")
print(np.matmul(smb.q2r(q), [1, 0, 0]), "\n")


q0 = smb.qunit([1, 0, 0, 0])
smb.qprint(q0)
print("\n")

smb.qprint(smb.qslerp(q0, q, 0))
print("\n")


smb.qprint(smb.qslerp(q0, q, 1))
print("\n")

smb.qprint(smb.qslerp(q0, q, 0.5))
print("\n")