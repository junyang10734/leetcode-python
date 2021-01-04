# 310. Minimum Height Trees

# BFS / Graph
# https://blog.csdn.net/fuxuemingzhu/article/details/83548874
# running time: faster than 54.50%
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        leaves = collections.defaultdict(set)
        for u,v in edges:
            leaves[u].add(v)
            leaves[v].add(u)
            
        que = collections.deque()
        for u,vs in leaves.items():
            if len(vs) == 1:
                que.append(u)
        
        while n > 2:
            n -= len(que)
            for i in range(len(que)):
                node = que.popleft()
                for v in leaves[node]:
                    leaves[v].remove(node)
                    if len(leaves[v]) == 1:
                        que.append(v)
        
        return list(que)