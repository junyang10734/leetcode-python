# 186. Reverse Words in a String II
# Two Pointers

# https://leetcode.com/problems/reverse-words-in-a-string-ii/solution/
# runtime: O(n)
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """    
        def reverse(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        reverse(0, len(s)-1)
        
        start = 0
        for i,char in enumerate(s):
            if char == ' ':
                reverse(start, i-1)
                start = i + 1
        reverse(start, len(s)-1)
