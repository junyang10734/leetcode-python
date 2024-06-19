# 3Sum

# two points
# faster than 87.44%
# detail: https://www.youtube.com/watch?v=CW6G30xQCbw
# very good solution, notice it
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        
        for i in range(n-2):
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, n-1
            while l<r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp < 0:
                    l += 1
                elif tmp > 0:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l+1 < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    while l < r-1 and nums[r] == nums[r-1]:
                        r -= 1           
                    r -= 1
                    
        return res


# https://leetcode.com/problems/3sum/editorial/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}

        for i,v1 in enumerate(nums):
            if v1 not in dups:
                dups.add(v1)
                for j,v2 in enumerate(nums[i+1:]):
                    v3 = -v1-v2
                    if v3 in seen and seen[v3] == i:
                        res.add(tuple(sorted((v1, v2, v3))))
                    seen[v2] = i
        return res