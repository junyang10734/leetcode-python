# 503. Next Greater Element II
# Stack  单调递减栈
# 739

# https://zhenyu0519.github.io/2020/06/29/lc503/
# runtime: faster than 65.67% 
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        stack = []
        nums += nums
            
        for i in list(range(n))*2:
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        
        return res

# 单调栈 - 模板
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2*n-1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            
            if stack:
                res[i % n] = stack[-1]
            stack.append(nums[i % n])
        return res