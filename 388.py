# Longest Absolute File Path
# Stack

# https://blog.csdn.net/fuxuemingzhu/article/details/82841402
# runtime: faster than 70.36% 
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = [(-1,0)]
        max_len = 0
        
        for p in input.split('\n'):
            depth = p.count('\t')
            p = p.replace('\t','')
            
            while stack and depth <= stack[-1][0]:
                stack.pop()
            
            if '.' not in p:
                stack.append((depth, len(p) + stack[-1][1] + 1))
            else:
                max_len = max(max_len, len(p) + stack[-1][1])
        
        return max_len
