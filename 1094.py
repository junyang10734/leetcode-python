# 1094. Car Pooling
# Array / 差分数组


# 差分数组
# time: O(n)
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxD = 0
        for n,f,t in trips:
            maxD = max(maxD, t)
        
        diff = [0 for _ in range(maxD+1)]
        for n,f,t in trips:
            diff[f] += n
            diff[t] -= n
        
        used_capacity = 0
        for d in diff:
            used_capacity += d
            if used_capacity > capacity:
                return False
        
        return True