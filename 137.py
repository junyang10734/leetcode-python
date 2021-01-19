# Single Number II
# Array

# Sort
# runtime: faster than 62.62%
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)-3, 3):
            if nums[i] != nums[i+2]:
                return nums[i]
        
        return nums[-1]


# Hash Table
# running time: faster than 99.89% 
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                if dic[i] == 2:
                    dic.pop(i)
                else:
                    dic[i] += 1
        return dic.popitem()[0]


# Math
# concept: 3*(a+b+c)−(a+a+a++b+b+b+c)=2c
class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*(sum(set(nums))) - sum(nums))//2


# Counter
# running time: faster than 89.93%
class Solution4:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        for k,v in c.items():
            if v == 1:
                return k