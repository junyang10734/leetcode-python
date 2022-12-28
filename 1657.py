# 1657. Determine if Two Strings Are Close
# Hash Table / Set

# https://leetcode.com/problems/determine-if-two-strings-are-close/discuss/1029064/Python-Oneliner-with-Counter-explained
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) == set(word2):
            cnt1 = collections.Counter(word1)
            cnt2 = collections.Counter(word2)
            if Counter(cnt1.values()) == Counter(cnt2.values()):
                return True
        return False
