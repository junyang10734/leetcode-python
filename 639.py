# 639. Decode Ways II
# DP

# https://leetcode.com/problems/decode-ways-ii/discuss/105274/Python-Straightforward-with-Explanation
# runtime: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n1, n2, n3 = 1, 0, 0
        
        for char in s:
            if char == '*':
                t1 = 9 * n1 + 9 * n2 + 6 * n3
                t2 = n1
                t3 = n1
            else:
                t1 = (char > '0') * n1 + n2 + (char <= '6') * n3
                t2 = (char == '1') * n1
                t3 = (char == '2') * n1
            n1, n2, n3 = t1 % MOD, t2, t3
        
        return n1