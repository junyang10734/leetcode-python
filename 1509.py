# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves
# Array / Greedy / Sorting

# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/discuss/730567/JavaC%2B%2BPython-Straight-Forward

# Sort / Greedy
# runtime: O(nlogn)
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        return min(mx - mi for mi, mx in zip(nums[:4], nums[-4:]))