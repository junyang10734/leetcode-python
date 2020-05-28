# Find All Numbers Disappeared in an Array
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/53981307


# Iteration
# runtime: faster than 81.72%
class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = list(range(1, len(nums) + 1))
        res = []
        
        for i in nums:
            l[i-1] = 0
        for j in l:
            if j != 0:
                res.append(j)
        
        return res


# Mark by negative in same place
# runtime: faster than 46.50% 
class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        
        res = [i+1 for i in range(len(nums)) if nums[i] > 0]
        return res


# Set
# runtime: faster than 96.94%
class Solution3:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        numset = set(nums)
        for i in range(1, len(nums)+1):
            if i not in numset:
                res.append(i)
        return res
