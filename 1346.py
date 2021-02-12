# 1346. Check If N and Its Double Exist
# Array, Hash Table

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for n in arr:
            if n * 2 in d or (n % 2 == 0 and n // 2 in d):
                return True
            else:
                d[n] = 1
        return False