#! /usr/bin/env python
import math

class three:
    h   = 6.626e-34         # J*s
    k   = 1.381e-23         # J/K
    m   = 14*2*1.661e-27    # kg
    T   = 298               # K
    vq  = (h/math.sqrt(2*math.pi*m*k*T))**3

