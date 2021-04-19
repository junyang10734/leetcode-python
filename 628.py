# 628. Maximum Product of Three Numbers
# Array / Math

# https://leetcode.com/problems/maximum-product-of-three-numbers/solution/

# runtime: O(n)
class Solution1:
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2 = float('inf'), float('inf')
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        
        for n in nums:
            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
            
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif n > max2:
                max2, max3 = n, max2
            elif n > max3:
                max3 = n
                
        return max(min1*min2*max1, max1*max2*max3)        


# runtime: O(nlogn)
class Solution2:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])