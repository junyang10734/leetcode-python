# 45. Jump Game II
# Greedy
# Compare with 55

# labuladong
# runtime: faster than 98.66%
# Easier to understand
class Solution1:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        end, farest = 0, 0
        jumps = 0
        for i in range(N-1):
            farest = max(farest, nums[i] + i)
            if end == i:
                jumps += 1
                end = farest
        return jumps


# https://blog.csdn.net/fuxuemingzhu/article/details/84578893
# Sams as Solution1
class Solution2:
    def jump(self, nums: List[int]) -> int:
        cur = 0
        count = 0
        pos = 0
        while cur < len(nums) - 1:
            count += 1
            pre = cur
            while pos <= pre:
                cur = max(cur, pos + nums[pos])
                pos += 1
        return count 
