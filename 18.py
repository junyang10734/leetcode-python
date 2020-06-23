# 4Sum
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/83543296
# Two Pointers
# runtime: faster than 51.29%
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        i = 0
        while i < n - 3:
            j = i + 1
            while j < n - 2:
                k = j + 1
                l = n - 1
                remain = target - nums[i] - nums[j]
                while k < l:
                    if nums[k] + nums[l] > remain:
                        l -= 1
                    elif nums[k] + nums[l] < remain:
                        k += 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k+1]:
                            k += 1
                        while k < l and nums[l] == nums[l-1]:
                            l -= 1
                        k += 1
                        l -= 1
                
                while j < n - 2 and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            while i < n - 3 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        
        return res