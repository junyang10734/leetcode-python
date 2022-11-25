# 921. Minimum Add to Make Parentheses Valid
# similar: 1542

# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/181132/C%2B%2BJavaPython-Straight-Forward-One-Pass
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = 0
        for i in s:
            if i == ')' and right == 0:
                left += 1
            else:
                right += 1 if i == '(' else -1
        return left + right
