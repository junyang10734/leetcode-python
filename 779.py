# 779. K-th Symbol in Grammar
# Recursion

# https://leetcode.com/problems/k-th-symbol-in-grammar/discuss/630113/Two-python-sol-sharing-w-Comment
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        else:
            if k % 2 == 0:
                return 0 if self.kthGrammar(n-1, (k+1)//2) else 1
            else:
                return 1 if self.kthGrammar(n-1, (k+1)//2) else 0