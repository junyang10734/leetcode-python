# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/solution/


# DFS
# running time: faster than 22.88%
class Solution1:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        
        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(dfs(nei, target) for nei in graph[source])
        
        
        for u,v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u,v):
                return u,v
            graph[u].add(v)
            graph[v].add(u)


# https://blog.csdn.net/fuxuemingzhu/article/details/80487064
# Union-Find
# running time: faster than 99.24%
class Solution2:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        tree = [-1] * (len(edges) + 1)
        for edge in edges:
            a = self.findRoot(edge[0], tree)
            b = self.findRoot(edge[1], tree)
            if a != b:
                tree[a] = b
            else:
                return edge
            
    def findRoot(self, x, tree):
        if tree[x] == -1:
            return x
        else:
            root = self.findRoot(tree[x], tree)
            tree[x] = root
            return root
