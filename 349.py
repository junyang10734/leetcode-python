# Intersection of Two Arrays
# Array

# runtime: faster than 37.98% 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = set(nums1), set(nums2)
        if len(nums1) > len(nums2):
            a, b = set(nums2), set(nums1)
        
        res = []
        for i in a:
            if i in b:
                res.append(i)
        
        return res