# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:29:42 2024

@author: kkeramati
"""

import numpy as np
import control as co

G2 = co.tf([2,5],[1,2,3])
pole_zeroCan = co.minreal(G2)
print(pole_zeroCan)