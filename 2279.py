# 2279. Maximum Bags With Full Capacity of Rocks
# Greedy

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        notFull = []
        res = 0
        for i,j in zip(capacity, rocks):
            if i == j:
                res += 1
            else:
                notFull.append(i-j)
        
        notFull.sort()
        for item in notFull:
            if additionalRocks >= item:
                res += 1
                additionalRocks -= item
            else:
                break

        return res