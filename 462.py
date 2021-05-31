# 462. Minimum Moves to Equal Array Elements II
# Math

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/94923/2-lines-Python-2-ways
# runtime: O(nlogn)
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums) // 2]
        return sum(abs(num - median) for num in nums)
