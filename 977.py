# 977. Squares of a Sorted Array
# Array

# faster than 88.82%
class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n**2 for n in nums])


# Two Pointers
# https://blog.csdn.net/XX_123_1_RJ/article/details/86568877
# runtime: faster than 16.75%
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        i = 0   # j, i表示两个指针，分别从正负界限，指向负数部分，和正数部分
        while i < N and nums[i] < 0:
            i += 1
        j = i - 1
        
        res = []
        while j >= 0 and i < N:
            if nums[j]**2 < nums[i]**2:
                res.append(nums[j]**2)
                j -= 1
            else:
                res.append(nums[i]**2)
                i += 1
        
        while j >= 0:
            res.append(nums[j]**2)
            j -= 1
        while i < N:
            res.append(nums[i]**2)
            i += 1
        
        return res
