# Single Element in a Sorted Array
# Array / Binary Search


# https://blog.csdn.net/fuxuemingzhu/article/details/79275636

# 异或
# runtime: faster than 46.02%
class Solution1:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums)


# iterate 遍历
# runtime: faster than 96.90%
class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]


# Binary Search
# runtime: faster than 88.60%
class Solution3:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while(l<r):
            mid = l + (r-l)//2
            if mid%2 == 1:
                mid -= 1   
            if nums[mid] != nums[mid+1]:  # single element exists in the left
                r = mid
            else:  # single element exists in the right
                l = mid + 2
        return nums[l]