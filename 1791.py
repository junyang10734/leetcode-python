# 1791. Find Center of Star Graph
# Graph / Hash Table

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = {}
        for a,b in edges:
            if a in d:
                return a
            else:
                d[a] = 1
            
            if b in d:
                return b
            else:
                d[b] = 1