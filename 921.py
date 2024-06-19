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



class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # res 记录插入次数
        res = 0
        # need 变量记录右括号的需求量
        need = 0
        for i in s:
            if i == '(':
                # 对右括号的需求 + 1
                need += 1
            else:
                # 对右括号的需求 - 1
                need -= 1
                if need == -1:
                    need = 0
                    # 需插入一个左括号
                    res += 1
        return need + res