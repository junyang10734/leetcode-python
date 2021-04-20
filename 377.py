# 377. Combination Sum IV
# DP / Backtracking

# Backtracking
# TLE
class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count = 0
        def backtrack(path, s):
            nonlocal count
            for num in nums:
                if s + num == target:
                    count += 1
                elif s + num < target:
                    backtrack(path + [num], s+num)
        
        backtrack([], 0)
        return count

# https://leetcode.com/problems/combination-sum-iv/solution/
# DP
# runtime: O(TN)  T = target, N = the number of elements in the input array
class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for comb_sum in range(target+1):
            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum - num]
        return dp[target]