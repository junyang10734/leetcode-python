# 1218. Longest Arithmetic Subsequence of Given Difference
# DP


# TLE
# Time: O(n*n), Space: O(n)
class Solution1:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        N = len(arr)
        dp = [1] * N
        
        for i in range(N):
            for j in range(i+1, N):
                if arr[j] - arr[i] == difference:
                    dp[j] = max(dp[j], dp[i]+1)
                    break
                    
        return max(dp)


# Hash
# time: O(n)
# runtime: faster than 49.65%
# https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-1218-longest-arithmetic-subsequence-of-given-difference/
class Solution2:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = collections.defaultdict(int)
        res = 0
        for x in arr:
            dp[x] = dp[x-difference] + 1
            res = max(res, dp[x])
        return res