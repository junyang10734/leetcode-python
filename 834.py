# 834. Sum of Distances in Tree
# DFS

# https://leetcode.com/problems/sum-of-distances-in-tree/solutions/130583/c-java-python-pre-order-and-post-order-dfs-o-n/
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = collections.defaultdict(set)
        ret = [0] * n
        count = [1] * n

        for i,j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs1(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs1(i, root)
                    count[root] += count[i]
                    ret[root] += count[i] + ret[i]

        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    ret[i] = ret[root] - count[i] + (n - count[i])
                    dfs2(i, root)

        dfs1(0, -1)
        dfs2(0, -1)
        return ret