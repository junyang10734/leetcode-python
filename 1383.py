# 1383. Maximum Performance of a Team
# Greedy / Heap

# https://leetcode.com/problems/maximum-performance-of-a-team/solution/
# runtime: O(n * (logn + logk))
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr = list(zip(speed, efficiency))
        arr.sort(key=lambda x: x[1], reverse=True)

        res, total = 0, 0
        for i in range(k):
            total += arr[i][0]
            res = max(total * arr[i][1], res)
        
        for i in range(k, n):
            total += arr[i][0] - arr[i-k][0]
            res = max(total * arr[i][1], res)
            
        return res % (10**9+7)