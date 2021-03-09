# 133. Clone Graph
# Graph / DFS / BFS

# https://blog.csdn.net/fuxuemingzhu/article/details/88363919

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# DFS
# runtime: faster than 53.82%
class Solution1:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_copy = self.dfs(node, {})
        return node_copy
    
    def dfs(self, node, hashd):
        if not node:
            return None
        if node in hashd:
            return hashd[node]
        node_copy = Node(node.val, [])
        hashd[node] = node_copy
        for n in node.neighbors:
            n_copy = self.dfs(n, hashd)
            if n_copy:
                node_copy.neighbors.append(n_copy)
        return node_copy


# BFS
# runtime: faster than 94.46%
class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return node

        que = deque()
        hashd = {}
        que.append(node)
        node_copy = Node(node.val, [])
        hashd[node] = node_copy
        
        while que:
            n = que.popleft()
            if not n:
                continue
            for neigh in n.neighbors:
                if neigh not in hashd:
                    hashd[neigh] = Node(neigh.val, [])
                    que.append(neigh)
                hashd[neigh].neighbors.append(hashd[n])
        
        return node_copy