from math import factorial
from math import pow


class M_M_1:

    l = 0.0
    miu = 0.0
    s = 0
    n = 0


    rho = 0.0
    p0 = 0.0
    pn = 0.0
    Lq = 0.0
    L = 0.0
    Wq = 0.0
    W = 0.0

    def __init__(self, avg, miu, n):
        self.avg = avg
        self.miu = miu
        self.s = 1
        self.n = n
        self.rho = self.Ro()
        self.p0 = self.P0()
        self.pn = self.Pn()
        self.lq = self.Lq()
        self.l = self.L()
        self.wq = self.Wq()
        self.w = self.W()
        self.cn = self.Cn()

    def Ro(self):
        answer = self.l / (self.s * self.miu)
        return answer

    def Lq(self):
        answer = pow(self.avg, 2) / (self.miu * (self.miu - self.avg))
        return answer

    def P0(self):
        result = 1 - self.p0
        return result
    
    def Pn(self):
        result = (1 - self.pn) * pow(self.rho, self.n)
        return result

    def L(self):
        answer = self.avg / (self.miu - self.avg)
        return answer

    def Wq(self):
        answer = self.lq / self.avg
        return answer

    def W(self):
        answer = self.l / self.avg
        return answer

    def Cn(self):
        result = (pow(self.l/self.miu,self.n))
        return result
