# 266. Palindrome Permutation
# Hash Table

# runtime: O(n)
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = collections.Counter(s)
        n = 0
        for k,v in count.items():
            if v % 2 == 1:
                if n > 0:
                    return False
                n += 1
        return True