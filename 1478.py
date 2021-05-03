# 1478. Allocate Mailboxes
# DP

# https://leetcode.com/problems/allocate-mailboxes/discuss/685516/Python3-oror-Detailed-Explanation-and-Commented-Code
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        
        @lru_cache(None)
        def dfs(i,j,k):
            if k == 1:
                m = houses[(i+j)//2]
                return sum(abs(x-m) for x in houses[i:j+1])
            elif k == j - i + 1:
                return 0
            elif k > j - i + 1:
                return inf
            else:
                return min(dfs(i, x, 1) + dfs(x+1, j, k-1) for x in range(i, j))
        
        return dfs(0, len(houses)-1, k)