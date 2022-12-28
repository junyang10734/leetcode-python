# Subsets
# backtrack


# backtrack 模板
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, path):
            res.append(path.copy())

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
        
        backtrack(0, path)
        return res



# https://www.cnblogs.com/zuoyuan/p/3757238.html
# recursive
# runtime: faster than 98.78% 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recur(d, start, l):
            res.append(l)
            if d == len(nums):
                return
            else:
                for i in range(start, len(nums)):
                    recur(d+1, i+1, l+[nums[i]])
                
        res = []
        recur(0, 0, [])
        return res