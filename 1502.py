# 1502. Can Make Arithmetic Progression From Sequence
# Array / Sort

# Sort
# time: O(nlogn)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr)-1):
            if arr[i+1] - arr[i] != diff:
                return False
        return True
    

# Set
# time: O(n)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        minV, maxV = min(arr), max(arr)
        n = len(arr)
        if maxV - minV == 0:
            return True
        if (maxV - minV) % (n-1):
            return False
        
        diff = (maxV - minV) // (n-1)
        s = set()
        for num in arr:
            if (num - minV) % diff:
                return False
            s.add(num)
        return len(s) == n


# In-place
# time: O(n)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        minV, maxV = min(arr), max(arr)
        n = len(arr)
        if maxV - minV == 0:
            return True
        if (maxV - minV) % (n-1):
            return False
        
        diff = (maxV - minV) // (n-1)
        i = 0
        while i < n:
            if arr[i] == minV + diff * i:
                i += 1
            elif (arr[i] - minV) % diff:
                return False
            else:
                j = (arr[i] - minV) // diff
                if arr[i] == arr[j]:
                    return False
                arr[i], arr[j] = arr[j], arr[i]
        return True