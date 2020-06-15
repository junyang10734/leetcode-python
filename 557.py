# Reverse Words in a String III
# String

# runtime: faster than 41.20% 
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i[::-1] for i in s.split()])