# 852. Peak Index in a Mountain Array
# Array / Binary Search

# runtime: faster than 83.64%
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l+r)//2
            if arr[mid] < arr[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l


# runtime: faster than 63.33%
class Solution2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))


# runtime: faster than 83.64%
class Solution3:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i