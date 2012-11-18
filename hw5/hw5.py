import math
import matplotlib.pyplot as plt

Na = 200
Nb = 100
q = 100

def multiplicity(N, q):
    '''
    Multiplicity of an Einstein solid with N harmonic oscillators 
    and q energy quanta.
    '''
    return math.factorial(N + q -1) / (math.factorial(q) * math.factorial(N - 1))

def list_macro_states(Na, Nb, q):
    '''
    Create a list of the multiplicities of each Macro state of two weakly
    coupled Einstein solids. Where Na and Nb are the number of harmonic 
    oscillators in solid A and B. q is the total energy quanta of the system.
    '''
    macro_list = []
    A_list = []
    B_list = []
    for i in range(0, q + 1):
        mult_A = multiplicity(Na, i)
        mult_B = multiplicity(Nb, q + 1 - i)
        A_list.append(mult_A)
        B_list.append(mult_B)
        macro_list.append(mult_A * mult_B)
    return macro_list, A_list, B_list

def plot():
    l, dont, need = list_macro_states(Na, Nb, q)
    plt.plot(l)
    plt.xlabel('q')
    plt.ylabel('multiplicity')
    plt.show()

def make_table():
    l, mult_A, mult_B = list_macro_states(Na, Nb, q)
    for i in range(len(l)):
        print "| q = %s\t| mult_A = %.4g\t| mult_B = %.4g\t| mult_AB = %.4g\t|" % (i , mult_A[i], mult_B[i],  l[i])

## 2.24 gaussian

def gaussian(N, x):
    return (2**N)*((2/(N*math.pi))**.5)*math.exp(-2*x*x*(N-1)*(N**-2))

