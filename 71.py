# 71. Simplify Path
# Stack

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = ''
        p = path.split("/")

        for i in range(len(p)):
            if stack and p[i] == "..":
                stack.pop()
            elif p[i] and p[i] != '.' and p[i] != '..':
                stack.append(p[i])

        if not stack:
            return '/'
        while stack:
            res = '/' + stack.pop() + res
        return res
