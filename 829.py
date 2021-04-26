# 829. Consecutive Numbers Sum
# Math

# https://leetcode.com/problems/consecutive-numbers-sum/solution/

# runtime: O(N**0.5)
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        upper = ceil((2 * N + 0.25) ** 0.5 - 0.5) + 1
        for k in range(1, upper):
            if (N - (k+1)*k // 2) % k == 0:
                count += 1
        return count