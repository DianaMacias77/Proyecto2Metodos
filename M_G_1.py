from math import pow


class M_G_1:
    avg = 0.0
    miu = 0.0
    s = 0.0
    std_dev = 0.0

    rho = 0.0

    lq = 0.0
    p0 = 0.0
    l = 0.0
    wq = 0.0

    def __init__(self, avg, miu, std_dev, n):
        self.avg = avg
        self.miu = miu
        self.s = 1
        self.std_dev = std_dev
        self.n = n
        self.rho = self.Ro()
        self.p0 = self.P0()
        self.pn = self.Pn()
        self.lq = self.Lq()
        self.l = self.L()
        self.wq = self.Wq()
        self.w = self.W()


    def Ro(self):
        answer = self.avg / (self.s * self.miu)
        return answer

    def Lq(self):
        answer = (pow(self.avg, 2) * pow(self.std_dev, 2) + (pow(self.rho, 2))) / (2 * (1 - self.rho))
        return answer

    def P0(self):
        answer = 1 - self.rho
        return answer

    def Pn(self):
        answer = pow(self.rho, self.n) * self.p0
        return answer

    def L(self):
        answer = self.rho + self.lq
        return answer

    def Wq(self):
        answer = self.lq / self.avg
        return answer

    def W(self):
        answer = self.wq + (1 / self.miu)
        return answer
