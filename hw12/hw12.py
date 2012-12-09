import math
class C:
    k   = 1.381e-23     # J/k
    pi  = math.pi
    h   = 6.626e-34     # J*s
    c   = 3e8           # m/s
    # Stefan-Boltzmann
    sig = 5.67e-8       # W/(m**2 * K**4)

class one:
    V = 5
    T = 1700
    U = (8./15.)* C.pi**5 * (C.k*T)**4 * V / (C.h * C.c)**3
    S = (32./45.)* C.pi**5 * V * (C.k * T/(C.h * C.c))**3

def N_photons(x):
    return x*x/(math.exp(x) - 1)

def integrate(n_max, h):
    n_max = float(n_max)
    h = float(h)
    N = n_max/h
    sum = 0
    for i in range(int(N)):
        sum += N_photons((i+1)*h) * h
    return sum

one_b = 8. * C.pi * one.V * (C.k*one.T/(C.h*C.c))**3 * integrate(30, .0001)

class two(C):
    R = 800
    A = 10e-6
    V = 120
    nu = 0.4

