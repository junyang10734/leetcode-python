# 1209. Remove All Adjacent Duplicates in String II
# Stack

# runtime: faster than 53.92%
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[s[0], 1]]
        for i in range(1, len(s)):
            if not stack or s[i] != stack[-1][0]:
                stack.append([s[i], 1])
            elif stack[-1][1] == k-1:
                    stack.pop()
            else:
                stack[-1][1] += 1

        res = ''
        for r,c in stack:
            res += r*c
        
        return res
                