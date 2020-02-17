# 3Sum

# brute, time limit exceeded
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        res = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]                    
                if (-sum) in nums[j+1:]:
                    l = [nums[i], nums[j], -sum]
                    l.sort()
                    if l not in res:
                        res.append(l)

        return res



# two points
# faster than 87.44%
# detail: https://www.youtube.com/watch?v=CW6G30xQCbw
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