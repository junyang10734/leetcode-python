# 797. All Paths From Source to Target
# BFS

# runtime: faster than 96.27%
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
                else:
                    stack.append([nx, path + [nx]])
        
        return res
                

# traverse - labuladong
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.destination = len(graph)-1

        def traverse(s, path):
            path.append(s)
            if s == self.destination:
                # if use path instead of path.copy(), when the path changes, the res will change too (传引用)
                res.append(path.copy())
            
            for neighbor in graph[s]:
                traverse(neighbor, path)
            
            path.pop()

        traverse(0, [])
        return res