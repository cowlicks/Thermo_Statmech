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
    def foo():
        k   = 8.617e-5          # eV/K
        B   = 1./(k*298)        # Beta
        n   = [0, 1, 2, 3]      # number of particles
        dE_list  = [0.001, 0.01, 0.1, 1.]   # epsilon - mu

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

class seven:
    h   = 6.626e-34         # J*s
    k   = 1.381e-23         # J/K
    Na  = 6.022e23          # Avogadro
    u   = 1.661e-27         # kg
    mcu = 63.346*u          # kg
    me  = 9.109e-31         # kg
    rho = 8.02e3            # kg/m3
    # Fermi energy
    ef = (h*h/(8*me))*(3*rho/(math.pi*mcu))**(2./3.)
    # Fermi Temperature
    Tf = ef/k
    # The electron degeneracy pressure
    P = (2./5.)*rho*ef/mcu

class eight:
    me  = 9.10938e-31
    mp  = 1.67262e-27
    k   = 1.381e-23         # J/K
    G   = 6.67300e-11
    h   = 6.626e-34
    c   = 3e8
    M   = 2e30
    R   = 0.02933*h*h/(me*(mp**(5./3.))*G*(M**(1./3.)))
    rho = M/((4./3.)*math.pi*R*R*R)
    ef  = (h*h/(8*me))*(9 * M/(8 * mp * math.pi**2 * R**3))**(2./3.) 
    Tf  = ef/k
    Mu  = ((13.7496)*me*c*(mp**(4./3.))*R/h)**(3./4.)

class nine:
    Na  = 6.022e23
    h   = 6.626e-34
    u   = 1.661e-27
    k   = 1.381e-23         # J/K
    NV  = Na*(100)**3 /37.
    mh3 = 3*u
    ef  = (h*h/(8*mh3))*(3*NV/math.pi)**(2./3.)
    Tf  = ef/k
    Cv  = math.pi**2 * k/(2*ef)
