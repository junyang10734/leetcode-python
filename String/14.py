# Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        pref = strs[0]
        for item in strs:
            while item.find(pref) != 0:
                pref = pref[:-1]
        
        return pref