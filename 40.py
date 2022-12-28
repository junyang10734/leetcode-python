# 40. Combination Sum II
# backtrack

# 模板
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                    backtrack(i+1)
                    path.pop()
                    pathSum -= candidates[i]
        
        backtrack(0)
        return res