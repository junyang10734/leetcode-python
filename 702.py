# 702. Search in a Sorted Array of Unknown Size
# Binary Search

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/solution/
# runtime: O(logn)
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0
        
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1
        
        while left <= right:
            mid = left + (right - left) // 2
            num = reader.get(mid)
            
            if num == target:
                return mid
            elif num > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1