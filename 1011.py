# 1011. Capacity To Ship Packages Within D Days

# binary search
# https://blog.csdn.net/qq_32424059/article/details/88666260
# running time: faster than 83.61%
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)
        
        while l <= r:
            mid = (l + r) // 2
            tmp = 0
            day = 1
            
            for w in weights:
                tmp += w
                if tmp > mid:
                    day += 1
                    tmp = w
            
            if day > D:
                l = mid + 1
            elif day <= D:
                r = mid - 1
                
        return l