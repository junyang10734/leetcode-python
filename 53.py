# 分治
# The basic idea is to partition A into two halves A1 and A2. 
# Then the contiguous subsequence with maximum sum could be (1) in A1, (2) in A2 or (3) part of it in A1 and the other part in A2. 
# We use recursive calls to deal with case (1) and case (2). 
# For case (3), we can grow the subsequence from A[⌊n/2⌋] forward and backward and choose the one with maximum sum. 
class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.dac(nums, 0, len(nums)-1)
    
    def dac(self, nums, left, right):
        if left==right:
            return nums[left]
        else:
            mid = int((left+right)/2)
            sl = self.dac(nums,left,mid)
            sr = self.dac(nums,mid+1,right)
            
            sc1 = nums[mid]
            maxsc1 = 0
            i = mid
            while(i>=left):
                maxsc1 = maxsc1 + nums[i]
                if maxsc1 > sc1:
                    sc1 = maxsc1
                i = i - 1
            
            sc2 = nums[mid+1] 
            maxsc2 = 0
            i = mid+1
            while(i<=right):
                maxsc2 = maxsc2 + nums[i]
                if maxsc2 > sc2:
                    sc2 = maxsc2
                i = i + 1

            return max(sl,sr,sc1+sc2)


# 动态规划
# dp[i]表示包含nums[i]的最大子数组和
# 迭代公式： dp[i] = max(nums[i], nums[i]+dp[i-1])
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        if len(nums) == 1:
            return sum
        else:
            dp = [0]*len(nums)
            dp[0] = nums[0]
            for i in range(1,len(nums)):
                dp[i] = max(nums[i], nums[i]+dp[i-1])

            return max(dp)