# 1541. Minimum Insertions to Balance a Parentheses String
# similar: 921

# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/discuss/780199/JavaC%2B%2BPython-Straight-Forward-One-Pass
class Solution:
    def minInsertions(self, s: str) -> int:
        res = right = 0 
        for i in s:
            if i == '(':
                right += 2
                if right % 2:
                    res += 1
                    right -= 1
            elif i == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return res + right


class Solution:
    def minInsertions(self, s: str) -> int:
        res, need = 0, 0
        for i in s:
            if i == '(':
                need += 2
                if need % 2 == 1:
                    res += 1
                    need -= 1
            else:
                need -= 1
                if need == -1:
                    res += 1
                    need = 1

        return res + need
