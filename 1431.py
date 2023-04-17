# 1431. Kids With the Greatest Number of Candies
# Array

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        res = []
        for candy in candies:
            if candy + extraCandies >= maxCandies:
                res.append(True)
            else:
                res.append(False)
        
        return res
