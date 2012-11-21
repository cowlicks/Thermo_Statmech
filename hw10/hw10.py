import math
import pylab
import numpy

def s(x):
    print "%.4g" % x
# Problem 2 schroeder 6.21
def E(n):
    return 1.03*n - 0.03*n*n
def Exp(n,g):
    return math.exp(-E(n)/g)

def Cv(g, n=15):
    sum_a = 0
    sum_b = 0
    sum_c = 0

    for i in range(n+1):
        sum_a += (E(n)**2) * Exp(n,g)
        sum_b += E(n)*Exp(n, g)
        sum_c += Exp(n, g)
    return (1./(g*g))*((sum_a)*(sum_c) - (sum_b)**2)/(sum_c**2)

# Plot this 
def zj(g , j=200):
    sum = 0
    g = float(g)
    for i in range(j+1):
        sum += (2*j + 1)*math.exp(-j*(j+1.)/g)
    return sum

# Plot = numpy.arange(1., 50000., 20.)
z = []
t = numpy.arange(10, 200., 1)
#t = range(0, 30)
for i in t:
    z.append(Cv(i))

pylab.close()
pylab.plot(t, z)
pylab.title('Partition function')
pylab.show()

class three:
    pass

class four:
    # Given:
    N = 3e21            # molecules
    k = 8.6173324e-5    # eV
    T = 1200            # K
    nu = 5.63e13        # Hz
    # Bond length
    Re = 0.115e-9       # m
    # Part a
    h = 4.1356675e-15   # eV*s
    eps_vib = h*nu      # h*nu
    beta = 1/(k*T)      # 1/kT
    beta_J = beta*6.24e18
    # P or fraction in second vibrational level.
    P = (1 - math.exp(-eps_vib*beta))*math.exp(-2*eps_vib*beta)
    
    # Part b
    hbar = 1.054572e-34 # J*s
    amu = 1.661e-27     # kg
    mn = 14.            # amu
    mo = 16.            # amu
    # Reduced mass
    mu = amu*(mn*mo)/(mn + mo)  # kg
    # Rotational energy quantum
    eps_rot = hbar**2 / (2*mu*Re**2)

    # Part c
    Utrans = N*k*T
    Urot = N*beta
    Uvib = N*eps_vib/(math.exp(eps_vib*beta) - 1)

class six:
    # From last problem
    N = 3.e21
    T = 1200.
    nu = 5.63e13
    kb_j = 1.380649e-23
    kb_ev = 8.61733e-5

    eps_vib = 6.6260696e-34*nu
    T_vib = 2701.97
    Svib = N*kb_j*(((T_vib/T)/(math.exp(T_vib/T) - 1)) - math.log(1 - math.exp(-T_vib/T)))

    eps_rot = 3.902397e-23
    T_rot = 2.4599
    Srot = N*kb_j*(1 + math.log(T/T_rot))
