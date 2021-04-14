# 667. Beautiful Arrangement II
# Array

# https://leetcode.com/problems/beautiful-arrangement-ii/solution/
# runtime: O(n)
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k == 1:
            return [i for i in range(1, n+1)]
        
        arr = [i for i in range(1, n-k)]
        for i in range(k+1):
            if i % 2 == 0:
                arr.append(n-k+i//2)
            else:
                arr.append(n-i//2)

        return arr
