# 77. Combinations
# Array / Recursive / Backtracking


# backtrack 模板
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(index):
            nonlocal k
            nonlocal n

            if len(path) == k:
                res.append(path.copy())
                return
            
            for i in range(index, n+1):
                path.append(i)
                backtrack(i+1)
                path.pop()
        
        backtrack(1)
        return res


# https://blog.csdn.net/fuxuemingzhu/article/details/79515180

# recursive
# running time: faster than 83.44%
class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(range(1,n+1), k, res, [])
        return res
    
    def helper(self, arr, k, res, path):
        if k > len(arr):
            return
        if k == 0:
            res.append(path)
        else:
            self.helper(arr[1:], k-1, res, path + [arr[0]])
            self.helper(arr[1:], k, res, path)


# backtracking
# running time: faster than 77.75%
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(range(1, n+1), k, res, [])
        return res
    
    def helper(self, arr, k, res, path):
        if k > len(arr):
            return
        if k == 0:
            res.append(path)
        else:
            for i in range(len(arr)):
                self.helper(arr[i+1:], k-1, res, path + [arr[i]])