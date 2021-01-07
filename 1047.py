# 1047. Remove All Adjacent Duplicates In String
# Stack

# running time: faster than 86.93% 
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if stack and s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
        
        return ''.join(stack)