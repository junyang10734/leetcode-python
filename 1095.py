# 1095. Find in Mountain Array
# Array / Binary Search

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# https://leetcode.com/problems/find-in-mountain-array/discuss/317607/JavaC%2B%2BPython-Triple-Binary-Search
# runtime: O(logn)
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()
        l, r = 0, N-1
        while l < r:
            m = (l+r)//2
            if mountain_arr.get(m) < mountain_arr.get(m+1):
                l = peak = m + 1
            else:
                r = m
                
        l, r = 0, peak
        while l <= r:
            m = (l+r)//2
            num_m = mountain_arr.get(m)
            if num_m == target:
                return m
            elif num_m < target:
                l = m + 1
            else:
                r = m -1
        
        l, r = peak, N-1
        while l <= r:
            m = (l+r)//2
            num_m = mountain_arr.get(m)
            if num_m == target:
                return m
            elif num_m > target:
                l = m + 1
            else:
                r = m -1
        
        return -1