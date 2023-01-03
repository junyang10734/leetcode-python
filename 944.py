# 944. Delete Columns to Make Sorted
# Array

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for j in range(len(strs[0])):
            arr = []
            for i in range(len(strs)):
                arr.append(strs[i][j])
                if i >= 1:
                    if arr[-1] < arr[-2]:
                        res += 1
                        break
        
        return res