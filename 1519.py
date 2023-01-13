# 1519. Number of Nodes in the Sub-Tree With the Same Label
# BFS / DFS

# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/solutions/743150/clean-python-3-dfs-with-counter/?orderBy=most_votes
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = collections.defaultdict(list)
        for a,b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        res = [0] * n

        def dfs(node, parent):
            counter = collections.Counter()
            for child in tree[node]:
                if child == parent:
                    continue
                counter += dfs(child, node)
            counter[labels[node]] += 1
            res[node] = counter[labels[node]]
            return counter
        
        dfs(0, None)
        return res