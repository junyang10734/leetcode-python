# 1823. Find the Winner of the Circular Game
# Array


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        start = 0
        while len(arr) > 1:
            end = (start + k - 1) % n
            del arr[end]
            start = end
            n -= 1
        return arr[0]