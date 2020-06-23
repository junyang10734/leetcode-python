# Maximum XOR of Two Numbers in an Array
# Bit Manipulation

# https://blog.csdn.net/fuxuemingzhu/article/details/79473171
# runtime: faster than 83.83%
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = mask = 0
        for x in range(32)[::-1]:
            mask += 1 << x
            preSet = set([n & mask for n in nums])
            temp = ans | 1 << x
            for pre in preSet:
                if temp ^ pre in preSet:
                    ans = temp
                    break
        return ans