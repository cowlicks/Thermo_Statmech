from scipy import constants as C
from math import pi
# Problem 1
class p1:
    Pi = 0.13333
    Vi = 1e-3
    T = 300.
    Kb = C.Bolzmann
    # Nitrogen diameter and scattering cross section.
    N2_d = 0.3e-9
    N2_sigma = pi * N2_d**2
    # Number density n = N/V = P /(Kb * T)
    n = Pi / (Kb * T)
    # Mean free path
    l = 1. / (2**.5 * n * N2_sigma)

    # Part d.
    # Diameter of hole and area.
    d_hole = 0.5e-3
    A_hole = d_hole**2 * pi
    # Distance to plate.
    d_disk = 0.3
    r_plate = 0.01 * .5
    A_plate = r_plate**2 * pi
    # Mass of nitrogen.
    m = 4.65e-26
    alpha = m / (2*Kb*T)
    vbar = (pi / alpha)**.5 * (3./4)
    Fplate = .25 * n * vbar * A_hole * pi * (r_plate / d_disk)**2 * 2 * vbar * m
    # e
    thalf = 4 * Vi /(A_hole * vbar)

class p3:
    # Given.
    A = .3 * 1
    b = 2e-3
    P = 101e3
    Tin = 295.372
    Tout = 255.372
    dT = 40
    Tavg = (Tin + Tout)/2
    dn2 = .36e-9

    # lookup
    kb = 1.38065e-23
    NA = 6.022141e23
    Cv = 20.786

    # n2 x section
    n2sig = pi * dn2**2
    # n2 mass
    mn2 = 39.948e-3 * (1./ NA)
    
    # Need.
    n = P/(kb * Tavg) 
    vbar = (8 * kb * Tavg /(pi * mn2))**.5
    l = 1./((2**.5) * n * n2sig)

    #formulas
    kt = 1.227 * n * vbar * l * Cv / NA
    dqdt = kt * A * dT / b


class p4:
    # Given.
    mp = .03
    dpuck = 8e-2
    hpuck = 0.2e-3
    P = 101325.
    T = 295.
    dn2 = 0.4e-9
    # Part a
    v0 = 20
    A_puck = (.5 * dpuck)**2 * pi
    m_n2 = 4.65e-26
    n2_x_sctn = dn2**2 * pi
    vbar = (8 * C.Bolzmann * T / (pi * m_n2))**.5

    # eta, the viscosity
    viscosity = 0.347 * m_n2 * vbar / n2_x_sctn
    # Drag force.
    Fdrag = -viscosity * A_puck * v0 / hpuck

    def visc(molecule_mass, avg_v, molecule_xs_sctn):
        return 0.347 * molecule_mass * avg_v / molecule_x_sctn

    def drag_force(viscosity, area , v0, distance):
        return -viscosity * area * v0 / distance

    # part b
    x = 2
    alpha = viscosity * A_puck / (mp * hpuck)
    c = -x
    b = v0 - x
    a = (alpha * v0 - (v0 / 2))
    tp = (-b + (b*b - 4 * a * c)**.5)/ (2 * a)
    tm = (-b - (b*b - 4 * a * c)**.5)/ (2 * a)
    vp = v0 /(1 + alpha*tp)
    vm = v0 /(1 + alpha*tm)

class p5:
    l = 63e-9
    vbar = 470
    Dslf = 0.6002*l*vbar
    t = 4*4 / (2 * Dslf)



