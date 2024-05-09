# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:34:16 2024

@author: kkeramati
"""

import roboticstoolbox as rtb
import numpy as np
import spatialmath.base as smb
import spatialmath as sm
import matplotlib.pyplot as plt
## 0:45
# T0 = np.identity(4)

# T1 = np.matmul(smb.transl(1,1,1), smb.rpy2tr(0.1, 0.1, 0.1, order = 'xyz'))

# # 1:36
# smb.trplot(T0)
# plt.show()

# # 1:39
# smb.trplot(T1)
# plt.show()

# # 1:53
# T0 = sm.SE3(T0)
# T1 = sm.SE3(T1)
# traj = rtb.ctraj(T0, T1, t=100)
# smb.tranimate(traj)

# ### 1D polynominal trajectory

# tg = rtb.tools.trajectory.quintic(0, 1, 50)
# tg.plot()
# s , sd, sdd = tg.s , tg.sd, tg.sdd

# # print(rtb.tools.trajectory.quintic(0, -1, 50).s, "\n")
# # rtb.tools.trajectory.quintic(0, -1, 50).plot()



# tg_v = rtb.tools.trajectory.quintic(0, 1, 50, 0.5, 0)
# sv, sv_d, sv_dd = tg_v.s, tg_v.sd, tg_v.sdd
# tg_v.plot()
# ### 1D trapezodial trajectory
# tg_trp= rtb.tools.trajectory.trapezoidal(0, 1, 50,0.035)
# s_trp,sd_trp,sdd_trp = tg_trp.s, tg_trp.sd, tg_trp.sdd
# tg_trp.plot()




### ### 1D trajectory with via points

# first = 10
# last = 30
# via = np.asarray([[40],[10],[last]])

# traj = rtb.mstraj(via, 0.1,2,qdmax=1,q0 = first)
# plt.plot(traj.q)
# plt.show()
# traj = rtb.mstraj(via, 0.1, 4, qdmax = 1, q0 = first)
# plt.plot(traj.q)
# plt.show()
# traj = rtb.mstraj(via, 0.1, 8, qdmax = 1, q0 = first)
# plt.plot(traj.q)
# plt.show()
# traj = rtb.mstraj(via, 0.1, 0, qdmax = 1, q0 = first)
# plt.plot(traj.q)
# plt.show()

# traj = rtb.mstraj(via, 0.1, 4, qdmax = 1, q0 = first)
# plt.plot(traj.q)
# plt.show()
# traj = rtb.mstraj(via, 0.1, 4, qdmax = 2, q0 = first)
# plt.plot(traj.q)
# plt.show()

# traj = rtb.mstraj(via,0.1,4, tsegment=[10,20,30], q0=first)

###Multi Dimentional###

# first = [10 , 20]
# last = [30 , 10]

# x = rtb.jtraj(first, last ,50) # joint interpolate trajectory
# x.plot()

# x = rtb.jtraj(first, last, 50, qd0 = [0,0], qd1=[10,10])
# x.plot()

# start = [40, 50]
# via = np.asarray([[60,30],[40,10],[20,30],start])
# # x = rtb.mstraj(via, 0.1, 1,qdmax=2,q0 = start)
# # plt.figure()
# # plt.plot(x.q[:,:])

# # plt.figure()
# # plt.plot(x.q[:,0],x.q[:,1])

# x = rtb.mstraj(via,0.1, 1, qdmax= [1,3], q0 = start)

# plt.figure()
# plt.plot(x.q)
# plt.figure()
# plt.plot(x.q[:,0],x.q[:,1])

# ############# Interpolating rotation in 3D ###########
# x = rtb.jtraj([0, 0, 0], [-np.pi / 2, np.pi / 2, np.pi / 4], 100)

# x.plot()

# R = [smb.rpy2r(q) for q in x.q]

# print(R[0], "\n")

# print(R[10], "\n")

# smb.tranimate(R)

# q1 = smb.qunit([1, 0, 0, 0])
# smb.qprint(q1)
# print("\n")

# q2 = smb.qunit(smb.r2q(smb.rotx(np.pi / 2)))
# smb.qprint(q2)
# print("\n")

# smb.qprint(smb.qslerp(q1, q2, 0))
# print("\n")

# smb.qprint(smb.qslerp(q1, q2, 1))
# print("\n")

# smb.qprint(smb.qslerp(q1, q2, 0.5))
# print("\n")

# print(smb.q2r(smb.qslerp(q1, q2, 0.5)))

############Interpolating pose in 3D ####
# T0 = sm.SE3()

# T1 = sm.SE3.Trans(1, 2, 3) * sm.SE3.RPY(0.6, 0.8, 1.4)

# T = rtb.ctraj(T0, T1, 50)

# print(T[0], "\n")

# print(T[10])

# smb.tranimate(T)