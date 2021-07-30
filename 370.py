# 370. Range Addition
# Array / Prefix Sum

# https://leetcode.com/problems/range-addition/solution/
# runtime: O(n+k)
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * length
        for i,j,n in updates:
            arr[i] += n
            if j < length-1:
                arr[j+1] -= n
        
        for i in range(1, length):
            arr[i] += arr[i-1]
        return arr