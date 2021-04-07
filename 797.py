# 797. All Paths From Source to Target
# BFS

# runtime: faster than 39.86%
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        res = []
        
        stack = [[0, [0]]]
        while stack:
            node, path = stack.pop(0)
            for nx in graph[node]:
                if nx == end:
                    res.append(path+[nx])
                stack.append([nx, path + [nx]])
        
        return res
                