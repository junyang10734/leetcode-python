# 905. Sort Array By Parity
# Array / Two Pointers

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A)-1
        while i < j:
            if A[i] % 2 == 0:
                i += 1
            elif A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            else:
                j -= 1
        return A