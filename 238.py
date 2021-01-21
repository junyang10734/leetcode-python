# Product of Array Except Self
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/79325534
# runtime: faster than 93.00%
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = len(nums)
        res = []
        p = 1
        for i in range(count):
            res.append(p)
            p *= nums[i]
        
        p = 1
        for j in range(count-1,-1,-1):
            res[j] *= p
            p *= nums[j]
        
        return res


# 计算总乘积，返回总乘积除以当前数值即可
# 遍历过程计算0的个数
# 若 > 1，则结果全部为0
# 若 == 1，则除了0，其他数的结果都为0
# 若 == 0, 无需特殊处理
# runtime: faster than 99.77%
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroCount = 0
        for i in nums:
            if i != 0:
                prod *= i
            else:
                zeroCount += 1
        
        res = []
        if zeroCount > 1:
            res = [0] * len(nums)
        elif zeroCount == 1:
            for i in nums:
                if i != 0:
                    res.append(0)
                else:
                    res.append(prod)
        else:
            for i in nums:
                res.append(prod//i)
        
        return res