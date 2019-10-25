# Reverse String

# two points: faster than 53.51% 
# space: O(1)
class Solution1(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        a, b = 0, len(s)-1
        while a < b:
            t = s[a]
            s[a] = s[b]
            s[b] = t
            a += 1
            b -= 1


# faster than 97.95%
class Solution2(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()