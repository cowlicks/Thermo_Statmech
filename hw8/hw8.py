import math
# 1 Brownian motion.
class one:
    d = 0.6e-6
    T = 293.15
    n = 0.01002
    t = 800
    xrms = 34.3e-6
    kb = xrms**2 * 3 * math.pi * n * (d/2) /(T*t)
    R = 8.315
    NA = R/kb

# 2 schroeder 4.2
class two:
    P = 1e9
    Thi = 773.15
    Tc = 293.15
    ei = 1 - Tc/Thi

    Thf = 783.15
    ef = 1 - Tc/Thf
    Qh = P/ei

# 3 Heat Engine
class three:
    P1 = 1e5
    V1 = 0.06
    T1 = 300
    V2 = V1
    P3 = 1e5
    V3 = .2
    R = 8.314
    n = P1 * V1 / (R * T1)
    T3 = P3 * V3 / (R * n)
    P2 = P3 * ((V3/V2)**(7./5))
    T2 = P2 * V2 /(n * R)
    W23 = (5./2.)*(P3 * V3 - P2 * V2)
    W31 = P1 * (V1 - V3)
    Q12 = n * R * (5./2.) * (T2 - T1)
    W = W23 + W31
    Qh = Q12
    e = W/Qh
    ecarnot = 1 - (T1 / T2)

# 6
class six:
    Th = 300.
    Tc = 273.15
    cop = Tc /(Th - Tc)
    Ef = 334.e-4
    Er = Ef / cop

# 7
class seven:
    V = 1.e-3
    T = 800
    P = 5e5
    R = 8.314
    n = P * V /(R * T)
    f = 3
    U = f * n * R * T
    H = U + P * V
    Na = 6.022141e23
    N = n*Na
    kb = 1.381e-23
    pi = math.pi
    m = 1.661e-27 * 40
    h = 6.626e-34
    S = N*kb*(math.log((V/N)*((4*pi*m*U/(3*N*h*h))**(3./2.))) + 5./2.)
    F = U - T*S
    G = U - T*S + P*V
    Vf = 3.e-3
    W = n*R*T*math.log(V/Vf)
    dS = n*R*math.log(Vf/V)
    Pf = n*R*T/Vf
    dH = Pf*Vf - P*V

# 8
class eight:
    dH = 2*(-285.83) + (-393.51) - (-74.81)
    dG = 2*(-237.13) + (-394.36) - (-50.72)
    Na = 6.022141e23
    V = dG/(8*Na)


