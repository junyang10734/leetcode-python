# 673. Number of Longest Increasing Subsequence
# compare: 300, 1048
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/79822126
# runtime: faster than 7.55%
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [(1,1)]*len(nums)
        longest = 1
        for i in range(1, len(nums)):
            curr_longest, cnt = 1, 0
            for j in range(i):
                if nums[j] < nums[i]:
                    curr_longest = max(curr_longest, dp[j][0] + 1)
            for j in range(i):
                if nums[j] < nums[i] and dp[j][0] == curr_longest - 1:
                    cnt += dp[j][1]
            dp[i] = (curr_longest, max(cnt, dp[i][1]))
            longest = max(longest, curr_longest)

        return sum([item[1] for item in dp if item[0] == longest])