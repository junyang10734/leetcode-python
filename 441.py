# Arranging Coins
# Math / Iteration / Binary Search

# https://blog.csdn.net/fuxuemingzhu/article/details/71330733

# Math
# runtime: faster than 98.60%
class Solution1:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(1+8*n) - 1) / 2)


# Iteration
# runtime: faster than 24.20% 
class Solution2:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        level = 0
        
        while count + level + 1 <= n:
            level += 1
            count += level
        return level


# Binary Search
# runtime: faster than 86.75%
class Solution3:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n + 1
        
        while left < right:
            mid = left + (right - left) / 2
            if mid * (mid + 1) / 2 <= n:
                left = mid + 1
            else:
                right = mid
            
        return int(left - 1)