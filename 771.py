# Jewels and Stones
# Hash Table

# https://blog.csdn.net/fuxuemingzhu/article/details/79188903

# runtime: faster than 39.28%
class Solution1:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = {}
        for j in J:
            d[j] = True
        
        num = 0
        for s in S:
            if s in d:
                num += 1
        
        return num


# runtime: faster than 0
class Solution2:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sCounter = collections.Counter(S)
        
        num = 0
        for j in J:
            num += sCounter[j]
        return num


# runtime: faster than 70.47%
class Solution3:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(j) for j in J)


# runtime: faster than 95.86% 
class Solution4:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        d = collections.defaultdict(int)
        for j in jewels:
            d[j] = 1
        
        for s in stones:
            if s in d:
                res += 1
        
        return res