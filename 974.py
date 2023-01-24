# 974. Subarray Sums Divisible by K
# Prefix Sum

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefixMod = 0
        modGroups = [0] * k
        modGroups[0] = 1

        for num in nums:
            prefixMod = (prefixMod + num % k + k) % k
            res += modGroups[prefixMod]
            modGroups[prefixMod] += 1
        
        return res
