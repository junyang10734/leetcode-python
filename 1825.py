# 1825. Finding MK Average
# Design


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.arr = []

    def addElement(self, num: int) -> None:
        self.arr.append(num)       

    def calculateMKAverage(self) -> int:
        n = len(self.arr)
        if n < self.m:
            return -1
        c = self.arr[n-self.m:]
        c.sort()
        new_c = c[self.k : (len(c)-self.k)]
        return sum(new_c) // len(new_c)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()