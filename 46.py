# Permutations

# https://blog.csdn.net/fuxuemingzhu/article/details/79363903

# recursive
# runtime: faster than 99.90% 
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.recur(nums, res, [])
        return res
    
    def recur(self, nums, res, path):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.recur(nums[:i] + nums[i+1:], res, path + [nums[i]])


# backtrack 模板
# runtime: faster than 94.29%
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [0] * len(nums)
        res = []
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        backtrack(path + [nums[i]])
                        visited[i] = 0
        backtrack([])
        return res