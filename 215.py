# Kth Largest Element in an Array

# Sort
# runtime: faster than 97.75% 
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


# https://blog.csdn.net/fuxuemingzhu/article/details/79264797
# 每次删除最大元素
# running time: faster than 13.50%
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k-1):
            nums.remove(max(nums))
        return max(nums)


# heapq 大根堆
# runtime: faster than 99.13% 
class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]