# Majority Element II
# Array

# runtime: faster than 95.89%
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = len(nums) // 3
        d = collections.defaultdict(int)
        for i in nums:
            d[i] += 1

        res = []
        for k in d:
            if d[k] > t:
                res.append(k)
        
        return res