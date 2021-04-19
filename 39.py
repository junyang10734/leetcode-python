# Combination Sum
# Array / Recursive / Backtracking


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