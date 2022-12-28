# Combination Sum
# Array / Recursive / Backtracking

# backtrack 模板
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path, pathSum = [], 0

        def backtrack(start):
            nonlocal pathSum
            if pathSum == target:
                res.append(path.copy())
                return
            elif pathSum > target:
                return
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    path.append(candidates[i])
                    pathSum += candidates[i]
                    backtrack(i)
                    path.pop()
                    pathSum -= candidates[i]
        
        backtrack(0)
        return res


# backtrack
# https://leetcode.com/problems/combination-sum/solution/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(remain, path, start):
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num == remain:
                    res.append(path + [num])
                elif num < remain:
                    backtrack(remain-num, path+[num], i)
                else:
                    continue
                    
        
        backtrack(target, [], 0)
        return res