# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:07:46 2024

@author: kkeramati
"""
from sympy import symbols, cos, sin, Matrix, diff, simplify, Function
from sympy.physics.mechanics import dynamicsymbols

# Define symbols for generalized coordinates
theta1, theta2 = dynamicsymbols('theta1 theta2')
dtheta1, dtheta2 = dynamicsymbols('theta1 theta2', 1)
ddtheta1, ddtheta2 = dynamicsymbols('theta1 theta2', 2)

# Link lengths, masses, and inertia
l1, l2, m1, m2, I1, I2, g = symbols('l1 l2 m1 m2 I1 I2 g')

# Positions of center of masses
x1 = l1/2 * cos(theta1)
y1 = l1/2 * sin(theta1)

x2 = l1 * cos(theta1) + l2/2 * cos(theta1 + theta2)
y2 = l1 * sin(theta1) + l2/2 * sin(theta1 + theta2)

# Velocities of center of masses
vx1 = diff(x1, theta1) * dtheta1
vy1 = diff(y1, theta1) * dtheta1

vx2 = diff(x2, theta1) * dtheta1 + diff(x2, theta2) * dtheta2
vy2 = diff(y2, theta1) * dtheta1 + diff(y2, theta2) * dtheta2

# Kinetic Energy
T1 = 1/2 * m1 * (vx1**2 + vy1**2) + 1/2 * I1 * dtheta1**2
T2 = 1/2 * m2 * (vx2**2 + vy2**2) + 1/2 * I2 * (dtheta1 + dtheta2)**2
T = simplify(T1 + T2)

# Potential Energy
V1 = m1 * g * y1
V2 = m2 * g * y2
V = simplify(V1 + V2)

# Lagrangian
L = simplify(T - V)

# Equations of Motion (Euler-Lagrange)
tau1 = diff(diff(L, dtheta1), 't') - diff(L, theta1)
tau2 = diff(diff(L, dtheta2), 't') - diff(L, theta2)

# Substitute dynamics symbols for time derivatives
tau1 = tau1.subs({
    diff(theta1, 't'): dtheta1,
    diff(theta2, 't'): dtheta2,
    diff(dtheta1, 't'): ddtheta1,
    diff(dtheta2, 't'): ddtheta2
})

tau2 = tau2.subs({
    diff(theta1, 't'): dtheta1,
    diff(theta2, 't'): dtheta2,
    diff(dtheta1, 't'): ddtheta1,
    diff(dtheta2, 't'): ddtheta2
})

tau1 = simplify(tau1)
tau2 = simplify(tau2)

# Output the equations of motion
print('Torque equations:')
print(f'Torque 1: {tau1}')
print(f'Torque 2: {tau2}')

# Example parameters (lengths in meters, masses in kg, inertias in kg*m^2, gravity in m/s^2)
example_parameters = {
    l1: 0.2, l2: 0.2,
    m1: 0.4, m2: 0.2,
    I1: 0.01, I2: 0.01,
    g: 9.81
}

# Substitute numerical values and evaluate example torques
torques = {
    tau1: tau1.subs(example_parameters),
    tau2: tau2.subs(example_parameters)
}

# Substitute angles and velocities for numerical calculations
theta_values = {
    theta1: 0.5, # 0.5 radian (~28.65 degrees)
    theta2: 0.3, # 0.3 radian (~17.19 degrees)
    dtheta1: 0.1,
    dtheta2: 0.2,
    ddtheta1: 0.05,
    ddtheta2: 0.1
}

# Calculate numerical torque values
numeric_torque1 = torques[tau1].subs(theta_values).evalf()
numeric_torque2 = torques[tau2].subs(theta_values).evalf()

print('\nNumerical Torque Results:')
print(f'Torque 1 (Nm): {numeric_torque1}')
print(f'Torque 2 (Nm): {numeric_torque2}')
