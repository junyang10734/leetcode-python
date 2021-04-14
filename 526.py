# 526. Beautiful Arrangement
# Array / Backtrack

# https://leetcode.com/problems/beautiful-arrangement/discuss/99738/Easy-Python-~230ms
class Solution:
    def countArrangement(self, n: int) -> int:
        def count(i, X):
            if i == 1:
                return 1
            arr = [count(i-1, X-{x}) for x in X if x % i == 0 or i % x == 0]
            return sum(arr)
        return count(n, set(range(1, n+1)))
