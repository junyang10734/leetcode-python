# 1726. Tuple with Same Product
# Array

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        N = len(nums)
        d = collections.defaultdict(list)
        
        for i in range(N-1):
            for j in range(i+1,N):
                prod = nums[i]*nums[j]
                d[prod].append((nums[i],nums[j]))

        res = 0
        for key,val in d.items():
            if len(val) > 1:
                res += len(val)*(len(val)-1)*4
        return int(res)
            