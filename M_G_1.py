from math import pow


class MG1:
    avg = 0.0
    miu = 0.0
    s = 0.0
    std_dev = 0.0

    ro = 0.0
    lq = 0.0
    ro0 = 0.0
    l = 0.0
    wq = 0.0

    def __init__(self, avg, miu, s, std_dev):
        self.avg = avg
        self.miu = miu
        self.s = s
        self.std_dev = std_dev

    def calculate(self):
        answer = {
            "Ro": self.Ro(),
            "Lq": self.Lq(),
            "L": self.L(),
            "Ro0": self.Ro0(),
            "Wq": self.Wq(),
            "W": self.W()
        }
        return answer

    def Ro(self):
        answer = self.avg / (self.s * self.miu)
        self.ro = answer
        return answer

    def Lq(self):
        answer = (pow(self.avg, 2) * pow(self.std_dev, 2) + (pow(self.ro, 2))) / (2 * (1 - self.ro))
        self.lq = answer
        return answer

    def Ro0(self):
        answer = 1 - self.ro0
        self.ro0 = answer
        return answer

    def L(self):
        answer = self.ro + self.lq
        self.l = answer
        return answer

    def Wq(self):
        answer = self.lq / self.avg
        self.wq = answer
        return answer

    def W(self):
        answer = self.wq + (1 / self.miu)
        self.w = answer
        return answer
