import math
class C:
    k   = 1.381e-23     # J/k
    kev = 8.617e-5
    pi  = math.pi
    h   = 6.626e-34     # J*s
    hev = 4.136e-15     # eV*s
    c   = 3e8           # m/s
    # Stefan-Boltzmann
    sig = 5.67e-8       # W/(m**2 * K**4)
    eV = 1.602e-19      # ev/j

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
    R = 800.
    A = 2*10e-6
    V = 120.
    nu = 0.4
    T = (V*V/(R*C.sig*nu*A))**(.25)
    Pr = V*V/R
    Emax = 2.82*C.kev*T
    lammax  = C.hev*C.c/Emax

def spectrum(e):
    return e**2 / (math.exp(e/(C.kev*two.T)) - 1)

def two_integrate(n_low, n_high, steps):
    sum = 0
    h = (n_high - n_low)/float(steps)
    for i in range(steps):
        sum += h*spectrum(n_low + h*(i+1))
    return sum

class three(C):
    V   = (1e-2)**3
    e1  = 1.
    e2  = 1.001
    m   = 0.5110e6      # eV/c
    gee = (math.pi/3.) * V * (8. * m/(C.hev**2))**(3./2.) * (e2**1.5 - e1**1.5)
    gep = (math.pi * 8. / 3.) * V * (1./(C.hev * C.c))**3 * (e2**3. - e1**3.)

class four(C):
    T1  = 1500
    T2  = 15e6
    P1  = (8.* math.pi**5 /45.)* (C.k * T1)**4 / (C.h * C.c)**3
    P2  = (8.* math.pi**5 /45.)* (C.k * T2)**4 / (C.h * C.c)**3
    Ph  = 1e5*C.k*T2/(1.6726e-27)

class six(C):
    So = 1370.
    sig = 5.67e-8
    e = .7
    Tg = (.25*So/(sig*(e-(2./3.))))**.25


