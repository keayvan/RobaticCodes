# -*- coding: utf-8 -*-
"""
Created on Tue May  7 09:31:31 2024

@author: kkeramati
"""

###3-Analayzing a very simple 1 joint robot arm###
import numpy as np
import matplotlib.pyplot as plt

class OneJointRobot:
    def __init__(self, length):

        self.length = length
        self.angle = 0

    def set_angle(self, angle):

        self.angle = np.deg2rad(angle)

    def get_end_effector_position(self):

        x = self.length * np.cos(self.angle)
        y = self.length * np.sin(self.angle)
        return (x, y)
    
    def get_transformation_matrix(self):
        
        tr = np.zeros([3,3])
        tr[0,:] = [ np.cos(self.angle),  -np.sin(self.angle), self.length * np.cos(self.angle)]
        tr[1,:] = [ np.sin(self.angle),  np.cos(self.angle), self.length * np.sin(self.angle)]
        tr[2,:] = [0 ,0, 1]
        return tr      

    def plot(self):
        """
        Plot the one-joint robot arm.
        """
        end_effector = self.get_end_effector_position()
        plt.figure()
        plt.plot([0, end_effector[0]], [0, end_effector[1]], marker='o')
        plt.xlim(-self.length, self.length)
        plt.ylim(-self.length, self.length)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("1-Joint Robot Arm")
        plt.grid(True)
        plt.show()
        
class nJointRobot:
    def __init__(self, length, angle):
        self.length = length
        self.angle = np.deg2rad(angle)
        
    def get_transformation_matrix(self):
        tr_all = np.identity(3)

        joint_pos = np.zeros([len(self.length),3,3])
        for i in range(len(self.length)):
            rot = np.asarray([[np.cos(self.angle[i]),  -np.sin(self.angle[i]), 0],[np.sin(self.angle[i]),  np.cos(self.angle[i]),0],[0,0,1]])
            trl = np.asanyarray([[1,0,self.length[i]],[0,1,0],[0,0,1]])
            tr = np.matmul(rot,trl)
            joint_pos[i] = tr
            tr_all=np.matmul(tr_all,tr)
        print (tr_all)
        return joint_pos, tr_all, [tr_all[0,-1],tr_all[1,-1]]
    def plot(self):

        joints, x, end_effector = self.get_transformation_matrix()
        plt.figure()
        jointi = np.zeros([joints.shape[0]+1,1,2])
        for i in range(joints.shape[0]):
            jointi[i+1] =  [joints[i,0,-1], joints[i,1,-1]]
        plt.plot(jointi[:,0,0],jointi[:,0,1], marker = 'o')
        return jointi 



if __name__ == "__main__":

    robot1 = nJointRobot([1,4,10], [20,30,20])
    joints, tr_matix, end_effector = robot1.get_transformation_matrix()
    joint1 = [joints[0,0,-1],joints[0,1,-1]]
    joint2 = [joints[1,0,-1],joints[1,1,-1]]
    
    jj = robot1.plot()
    # plt.plot(jj[:,0,0],jj[:,0,1])
    
