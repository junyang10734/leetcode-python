# 372. Super Pow
# Math / DaC


class Solution:
    base = 1337

    def myPow(self, a, k):
        a %= self.base
        res = 1
        for _ in range(k):
            res *= a
            res %= self.base
        return res

    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        part1 = self.myPow(a, last)
        part2 = self.myPow(self.superPow(a,b), 10)
        return (part1 * part2) % self.base
        


class Solution:
    def myPow(self, a, k):
        if k == 0:
            return 1
    
        base = 1337
        a %= base

        if k % 2 == 1:
            return (a * self.myPow(a, k - 1)) % base
        else:
            sub = self.myPow(a, k // 2)
            return (sub * sub) % base

    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        part1 = self.myPow(a, last)
        part2 = self.myPow(self.superPow(a,b), 10)
        return (part1 * part2) % 1337
        