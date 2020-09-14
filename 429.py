# N-ary Tree Level Order Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Recursion, BFS
# runtime: faster than 26.04%
# https://zxi.mytechroad.com/blog/tree/leetcode-429-n-ary-tree-level-order-traversal/
class Solution1:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        
        def helper(node, d, ans):
            if node == None:
                return 
            while len(ans) <= d:
                l = []
                ans.append(l)
            ans[d].append(node.val)
            for n in node.children:r
                helper(n, d+1, ans)
        
        
        helper(root, 0, ans)
        return 

# faster than 25.51%
# https://blog.csdn.net/fuxuemingzhu/article/details/81022170r
class Solution1:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if not node:
                    continue
                level.append(node.val)
                for child in node.children:
                    q.append(child)
            if level:
                res.append(level)
        return res


# DFS
# runtime: faster than 82.74%
# https://blog.csdn.net/fuxuemingzhu/article/details/81022170
class Solution2:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        self.getLevel(root, ans, 0)
        return ans

    def getLevel(self, node, ans, d):
        if not node:
            return []
        if d == len(ans):
            ans.append([])
        
        ans[d].append(node.val)
        for child in node.children:
            self.getLevel(child, ans, d+1)
        
        return ans
