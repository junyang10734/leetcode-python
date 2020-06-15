# Self Dividing Numbers
# Math

# runtime: faster than 8.26%
class Solution1:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        i = left
        res = []
        while i <= right:
            if i < 10:
                res.append(i)
            else:
                i = str(i)
                n = 0
                for s in i:
                    if int(s) == 0:
                        break
                    elif int(i) % int(s) == 0:
                        n += 1
                if n == len(i):
                    res.append(int(i))
            i = int(i)
            i += 1
        return res


# runtime: faster than 85.27%
class Solution2:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True
        
        res = []
        for n in range(left, right+1):
            if self_dividing(n):
                res.append(n)
        return res