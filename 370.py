# 370. Range Addition
# Array / Prefix Sum / 差分数组

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



class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0 for _ in range(length)]
        for start,end,num in updates:
            diff[start] += num
            if end < length-1:
                diff[end+1] -= num
        
        arr = [diff[0]]
        for i in range(1, length):
            arr.append(arr[-1] + diff[i])
        
        return arr