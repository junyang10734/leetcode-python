# 344. Reverse String
# Two Pointers / Recursion

# two points
# runtime: O(n)
class Solution1(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        a, b = 0, len(s)-1
        while a < b:
            s[a], s[b] = s[b], s[a]
            a += 1
            b -= 1


# Recursion
# runtime: O(n)
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(i, j):
            if i < j:
                s[i], s[j] = s[j], s[i]
                helper(i+1, j-1)
        
        helper(0, len(s)-1)


# built-in function
class Solution3(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()