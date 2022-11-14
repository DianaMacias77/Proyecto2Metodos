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
    pk = 0.0
    lq = 0.0
    l = 0.0
    le = 0.0
    wq = 0.0
    w = 0.0

    def __init__(self, avg, miu, s, k, n):
        self.avg = avg
        self.miu = miu
        self.k = k
        self.s = s
        self.n = n
        self.rho = self.Ro()
        self.p0 = self.P0()
        self.pn = self.Pn()
        self.pk = self.Pk()
        self.le = self.LambdaE()
        self.lq = self.Lq()
        self.wq = self.Wq()
        self.w = self.W()
        self.l = self.L()
        
        

    def Ro(self):
        answer = self.avg / (self.s * self.miu)
        return answer

    def Lq(self):
        side1 = (self.p0 * pow(self.avg / self.miu, self.s) * self.rho) / (factorial(self.s) * pow((1 - self.rho), 2))
        side2 = (1 - pow( self.rho, self.k - self.s) - ((self.k - self.s) * pow(self.rho, self.k - self.s) * (1-self.rho)))
        answer = side1 * side2
        return answer

    def P0(self):
        side1 = 0.0
        for i in range(self.s + 1):
            side1 += pow((self.avg / self.miu),i) / factorial(i)
        
        
        side2 = 0.0
        for i in range(self.s + 1 ,self.k + 1):
            side2 += pow(self.rho, i - self.s)
        side2 *= pow((self.avg / self.miu),self.s) / factorial(self.s)


        p0 = side1 + side2
        result = 1 / p0
        return result

    
    def Pn(self):
        if self.k > self.s:
            result = (pow(self.avg / self.miu, self.n) / (factorial(self.s) * pow(self.s, (self.n - self.s)))) * self.p0
        elif self.n < self.s or self.n >= 0:
            result = (pow((self.avg / self.miu), self.n)) / factorial(self.n)  * self.p0
        elif self.n > self.k:
            result = 0
        else:
            print("Error")
        return result

    def L(self):
        answer = self.le * self.w
        return answer

    def Wq(self):
        answer = self.lq / self.le
        return answer

    def W(self):
        answer = self.wq + (1 / self.miu)
        return answer

    def LambdaE(self):
        result = self.avg * (1 - self.pk)
        return result

    def Pk(self):
        answer = (pow(self.avg / self.miu, self.n) / (factorial(self.s) * pow(self.s, (self.n - self.s)))) * self.p0
        return answer