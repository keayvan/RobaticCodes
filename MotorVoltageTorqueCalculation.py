# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:58:45 2024

@author: kkeramati
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameters
R = 1.0       # Motor resistance (Ohms)
L = 0.01      # Motor inductance (H)
Ke = 0.01     # Back EMF constant (V/rad/s)
Kt = 0.01     # Torque constant (Nm/A)
J = 0.01      # Inertia of the arm (kg m^2)
B = 0.1       # Damping coefficient (Nm s/rad)
G = 10        # Gear ratio
V = 24        # Applied voltage (V)

# Differential equations
def motor_arm_dynamics(t, y):
    # State variables
    I = y[0]
    theta = y[1]
    omega = y[2]
    
    # Motor equation
    dIdt = (V - I * R - Ke * omega * G) / L
    
    # Motor torque
    Tm = Kt * I
    
    # Arm dynamics
    domegadt = (Tm * G - B * omega) / J
    dthetadt = omega
    
    return [dIdt, dthetadt, domegadt]

# Initial conditions: [current (A), angle (rad), angular velocity (rad/s)]
y0 = [0.0, 0.0, 0.0]

# Time span
t_span = (0, 2)
t_eval = np.linspace(0, 2, 1000)

# Solve the ODEs
solution = solve_ivp(motor_arm_dynamics, t_span, y0, t_eval=t_eval)

# Extract results
I = solution.y[0]
theta = solution.y[1]
omega = solution.y[2]
time = solution.t

# Plot the results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(time, I)
plt.xlabel('Time [s]')
plt.ylabel('Current [A]')
plt.title('Motor Current')

plt.subplot(3, 1, 2)
plt.plot(time, theta)
plt.xlabel('Time [s]')
plt.ylabel('Angle [rad]')
plt.title('Arm Angle')

plt.subplot(3, 1, 3)
plt.plot(time, omega)
plt.xlabel('Time [s]')
plt.ylabel('Angular Velocity [rad/s]')
plt.title('Arm Angular Velocity')

plt.tight_layout()
plt.show()
