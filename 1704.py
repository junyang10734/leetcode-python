# 1704. Determine if String Halves Are Alike
# String

# runtime: faster than 99.82%
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        a, b = s[:len(s)//2], s[len(s)//2:]
        count1, count2 = 0, 0
        for i in range(len(s)//2):
            if a[i] in vowels:
                count1 += 1
            if b[i] in vowels:
                count2 += 1
        return count1 == count2