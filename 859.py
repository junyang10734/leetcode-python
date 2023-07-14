# 859. Buddy Strings
# Hash Table


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            frequency = [0] * 26
            for ch in s:
                frequency[ord(ch) - ord('a')] += 1
                if frequency[ord(ch) - ord('a')] == 2:
                    return True
            return False

        firstIdx = -1
        secondIdx = -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if firstIdx == -1:
                    firstIdx = i
                elif secondIdx == -1:
                    secondIdx = i
                else:
                    return False
            
        if secondIdx == -1:
            return False
        return s[firstIdx] == goal[secondIdx] and s[secondIdx] == goal[firstIdx]