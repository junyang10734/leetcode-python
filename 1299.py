# 1299. Replace Elements with Greatest Element on Right Side
# Array

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        res.append(-1)
        maxN = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            if arr[i+1] > maxN:
                maxN = arr[i+1]
            res.append(maxN)
        return res[::-1]