from math import factorial
from math import pow


class M_Ek_1:

    l = 0.0
    miu = 0.0
    s = 0
    k = 0

    rho = 0.0

    p0 = 0.0
    pn = 0.0
    Lq = 0.0
    L = 0.0
    Wq = 0.0
    W = 0.0

    def __init__(self, avg, miu, k, n):
        self.avg = avg
        self.miu = miu
        self.k = k
        self.s = 1
        self.n = n
        self.rho = self.Ro()
        self.p0 = self.P0()
        self.pn = self.Pn()
        self.wq = self.Wq()
        self.w = self.W()
        self.lq = self.Lq()
        self.l = self.L()
        

    def Ro(self):
        answer = self.avg / (self.s * self.miu)
        return answer

    def Lq(self):
        answer = ((1 + self.k) / (2 * self.k)) * (pow(self.avg, 2) / (self.miu * (self.miu - self.avg)))
        return answer

    def P0(self):
        result = 1 - self.p0
        return result
    
    def Pn(self):
        result = pow(self.rho, self.n) * self.p0
        return result

    def L(self):
        answer = self.avg * self.w
        return answer

    def Wq(self):
        answer = self.lq / self.avg
        return answer

    def W(self):
        answer = self.wq + (1 / self.miu)
        return answer
