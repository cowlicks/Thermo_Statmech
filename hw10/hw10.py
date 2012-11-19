import math
# Boltzmann constant in ev/K
kb = 1.380649e-16
class two:
    # in eV
    e = .3          # energy quanta
    KbT = .025      # Boltzmans constant x temperature

    # Energy/energy quanta
    def E(self, n):
        n = float(n)
        return 1.03*n - 0.03*n*n
    def Z(self, n):
        sum = 0
        for i in range(n):
            sum += math.exp(-self.E(i)*self.e/self.KbT)
        return sum
    def avg_E(self, n):
        sum = 0
        for i in range(n):
            sum += E(i) * e * math.exp(-E(i) * e * (1./KbT))
        return sum/Z(n)
    def Cv(self, g, n = 15):
        sum_a = 0
        sum_b = 0
        sum_c = 0
        for i in range(n):
            sum_a += (E(n)**2) * math.exp(-E(n)/g)
            sum_b += E(n) * math.exp(-E(n)/g)
            sum_c += math.exp(-E(n)/g)
        return kb*(sum_a*sum_c - sum_b**2)/(g*g*(sum_c**2))
