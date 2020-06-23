# Minimum Moves to Equal Array Elements
# Math

# https://blog.csdn.net/fuxuemingzhu/article/details/54177981

# runtime: faster than 83.91%
class Solution1:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


# runtime: faster than 28.74% 
class Solution2:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for n in nums:
            res += n - nums[0]
        return res