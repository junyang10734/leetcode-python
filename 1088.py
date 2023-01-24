# 1088. Confusing Number II
# backtrack

# https://leetcode.com/problems/confusing-number-ii/solutions/408771/python-ugly-backtracking-solution/?orderBy=most_votes
class Solution:
    def confusingNumberII(self, n: int) -> int:
        validDigit = [0, 1, 6, 8, 9]
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        def backtrack(num, rotation, digit):
            res = 0
            if num != rotation:
                res += 1
            for d in validDigit:
                if d == 0 and num == 0:
                    continue
                if num * 10 + d <= n:
                    res += backtrack(num * 10 + d, mapping[d] * digit + rotation, digit * 10)
            return res
        
        return backtrack(0, 0, 1)
