# Range Sum Query - Immutable
# Array / Prefix Sum


# runtime: faster than 5.01% 
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        res = 0
        while i <= j:
            res += self.nums[i]
            i += 1
        return res


# https://blog.csdn.net/fuxuemingzhu/article/details/79253036

# runtime: faster than 81.75%
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        total = 0
        for i,val in enumerate(nums):
            total += val
            self.sums[i] = total
        

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i-1]   


# runtime: faster than 97.51%  
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            self.sums[i] = self.sums[i-1] + nums[i-1]
        

    def sumRange(self, i: int, j: int) -> int:
            return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)