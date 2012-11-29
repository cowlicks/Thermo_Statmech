#! /usr/bin/env python
import math

class three:
    h   = 6.626e-34         # J*s
    k   = 1.381e-23         # J/K
    m   = 14*2*1.661e-27    # kg
    T   = 298.              # K
    P   = 1.e5               # Pa 
    Na  = 6.022e23          # Avogadro
    # The quantum volume
    vq  = (h/math.sqrt(2*math.pi*m*k*T))**3
    # Average volume per molecule
    VN  = k*T/P
    # Quantum statistics applies where VN ~= vq. Or:
    Tq  = (P * (h**3) /((2*math.pi*m)**(3./2.) * k**(5./2.)))**(2./5.)

class five:
    # Fermi-Dirac probability of a state being occupied.
    def Pfd(self, e, u, b):
        return (math.exp(-(e-u)/float(b)) + 1)**-1




