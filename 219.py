# Contains Duplicate II
# Array / Hash Table

# runtime: faster than 13.32%
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i,num in enumerate(nums):
            if num in d:
                if i - d[num] <= k:
                    return True

            d[nums[i]] = i
        return False