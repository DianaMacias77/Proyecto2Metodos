from math import factorial
from math import pow


class M_M_S_K:

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

    def __init__(self, avg, miu, s, k, n):
        self.avg = avg
        self.miu = miu
        self.k = k
        self.s = s
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
        answer = self.avg / (self.s * self.miu)
        return answer

    def Lq(self):
        answer = (self.p0 * (pow((self.avg / self.miu), self.s)) * self.rho) / (factorial(self.s) * (pow((1  - self.rho), 2)))
        return answer

    def P0(self):
        res = 0.0
        for i in range(self.s):
            res += pow((self.avg / self.miu),i) / factorial(i)
        p0 = res + pow((self.avg / self.miu),self.s) / factorial(self.s)
        
        resK = 0.0
        for i in range(self.s + 1 ,self.k):
            resK += pow((self.avg / (self.s * self.miu)), self.n - self.s)
            
        p0 = p0 + resK
        result = pow(p0, -1)
        return result

    
    def Pn(self):
        if self.n < self.s or self.n >= 0:
            result = (pow((self.avg / self.miu), self.n)) / factorial(self.n)  * self.p0
        elif self.n >= self.s:
            result = (pow((self.avg / self.avg), self.n)) / (factorial(self.s) * pow(self.s, (self.n - self.s))) * self.p0
        else:
            print("Error")
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
