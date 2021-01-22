# 198. House Robber
# 动态规划
# dp[i]表示rob第i个房子的最大收益
# dp[i] = max(nums[i]+dp[i-2],dp[i-1])
# 注意dp[0]和dp[1]的初始化赋值

# run tims: O(n)  space: O(n)
class Solution1:
    def rob(self, nums: List[int]) -> int:
        account = len(nums)
        if account == 0 :
            return 0
        elif account == 1 :
            return nums[0]
        elif account == 2 :
            return max(nums)
        else:
            dp = [0] * account
            dp[0] = nums[0]
            dp[1] = nums[1] if nums[1] > dp[0] else dp[0]
            for i in range(2,account):
                dp[i] = max(nums[i]+dp[i-2],dp[i-1])
            return max(dp)


# run tims: O(n)  space: O(1)
class Solution2:
    def rob(self, nums: List[int]) -> int:
        account = len(nums)
        if account == 0 :
            return 0
        elif account == 1 :
            return nums[0]
        elif account == 2 :
            return max(nums)
        else:
            first = nums[0]
            second = nums[1] if nums[1] > first else first
            maxsum = second
            for i in range(2,account):
                maxsum = max(nums[i]+first,second)
                first = second
                second = maxsum
            return maxsum


# 更简洁的写法
# https://blog.csdn.net/fuxuemingzhu/article/details/51291936
# runtime: faster than 85.83% 
class Solution3:
    def rob(self, nums: List[int]) -> int:
            prev, curr = 0, 0
            for n in nums:
                prev, curr = curr, max(prev+n, curr)
            
            return curr
