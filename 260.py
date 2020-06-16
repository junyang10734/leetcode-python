# Single Number III
# Hash Table / Bit Manipulation


# Hash Table
# runtime: faster than 99.60%
class Solution1:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        res = []
        for k,v in c.items():
            if v == 1:
                res.append(k)
        
        return res


# Bit Manipulation
# runtime: faster than 53.43%
class Solution2:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        num1, num2 = 0, 0
        for n in nums:
            xor ^= n
        mask = 1
        while xor & mask == 0:
            mask = mask << 1
        for n in nums:
            if n & mask == 0:
                num1 ^= n
            else:
                num2 ^= n
        
        return [num1, num2]
