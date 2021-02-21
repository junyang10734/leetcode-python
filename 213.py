# 213. House Robber II
# 打家劫舍问题：198, 213, 337
# DP
# https://blog.csdn.net/fuxuemingzhu/article/details/82982325

# runtime: faster than 86.69%
class Solution1:
    def rob(self, nums: List[int]) -> int:
        # dp[0] = num[0] （当i=0时） 
        # dp[1] = max(num[0], num[1]) （当i=1时） 
        # dp[i] = max(num[i] + dp[i - 2], dp[i - 1]) （当i !=0 and i != 1时）
        if not nums:
            return 0
         
        N = len(nums)
        if N == 1:
            return nums[0]
        elif N == 2:
            return max(nums)
        else:
            return max(self.rob_range(nums[0: N-1]), self.rob_range(nums[1:N]))
        
    def rob_range(self, nums):
        if len(nums) == 2:
            return max(nums)
        else:
            dp = [0]*len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            
            return dp[-1]


# Less space
# runtime: faster than 65.18% 
class Solution2:
    def rob(self, nums: List[int]) -> int:      
        N = len(nums)
        if N == 1:
            return nums[0]
        elif N == 2:
            return max(nums)
        else:
            return max(self.rob_range(nums[0: N-1]), self.rob_range(nums[1:N]))
        
    def rob_range(self, nums):
        prev, curr = 0, 0
        for n in nums:
            prev, curr = curr, max(prev+n, curr)
        return curr


# labuladong
# Compare with 198
# runtime: faster than 87.18%
class Solution3:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        else:
            return max(self.helper(nums[1:]), self.helper(nums[:N-1]))
        
    def helper(self, nums: List[int]) -> int:
        dp_i1, dp_i2 = 0, 0
        dp_i = 0
        for i in range(len(nums)-1, -1, -1):
            dp_i = max(dp_i1, nums[i]+dp_i2)
            dp_i1, dp_i2 = dp_i, dp_i1
        return dp_i