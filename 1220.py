# 1220. Count Vowels Permutation
# DP

# https://leetcode.com/problems/count-vowels-permutation/solution/
# runtime: O(n)
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        MOD = 10 ** 9 + 7
        
        for k in range(1, n):
            new_a = (e + i + u) % MOD
            new_e = (a + i) % MOD
            new_i = (e + o) % MOD
            new_o = i % MOD
            new_u = (i + o) % MOD
            a, e, i, o, u = new_a, new_e, new_i, new_o, new_u
        
        return (a + e + i + o + u) % MOD