# 496. Next Greater Element I
# Stack 单调栈

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i,num in enumerate(nums2):
            d[num] = i
        
        n = len(nums2)
        stack = []
        arr = [-1] * n
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            
            if stack:
                arr[i] = stack[-1]
            stack.append(nums2[i])
        
        res = []
        for num in nums1:
            res.append(arr[d[num]])
        return res