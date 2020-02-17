# Jump Game

# greedy
# https://blog.csdn.net/fuxuemingzhu/article/details/83504437
# runtime: faster than 94.86%
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        for i,item in enumerate(nums):
            if step < i:
                return False
            step = max(step, i+item)
        return True