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
    k   = 8.617e-5          # eV/K
    # Fermi-Dirac probability of a state being occupied.
    def Pfd( dif, b=(1./(298*k))):
        return (math.exp(dif/float(b)) + 1)**(-1.)
    # (a)
    a = Pfd(-1.)
    # (b)
    b = Pfd(-0.01)
    # (c)
    c = Pfd(0.)
    # (d)
    d = Pfd(0.01)
    # (e)
    e = Pfd(1.)

class six:
    k   = 8.617e-5          # eV/K
    B   = 1./(k*298)
    n   = [0, 1, 2, 3]
    dE_list  = [0.001, 0.01, 0.1, 1.]

    for dE in dE_list:

        # Average occupancy.
        avgn = (math.exp(dE*B) - 1)**-1.
        print "Average ocuupancy at {} eV is {} particles".format(dE, avgn)
        print " and:"

        # Partition function.
        Z = (1 - math.exp(-dE*B))**-1.
        

        # Probability for state to have n[j] particles.
        for j in range(len(n)):
            P_sum = 0
            for k in range(j+1):
                P_sum += math.exp(-dE*B)
            P = (1./Z)*P_sum
            print "\t Probability of state containing {} bosons is {}".format(j, P)












