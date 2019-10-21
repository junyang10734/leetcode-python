# Implement strStr()
# solution1 is easier and more efficient than solution2
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1