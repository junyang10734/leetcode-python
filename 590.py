# N-ary Tree Postorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# DFS
# Recursive
# runtime: faster than 41.37% 
# https://blog.csdn.net/fuxuemingzhu/article/details/81017965
class Solution1:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        res = []
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        
        return res

# runtime: faster than 97.81% 
class Solution1:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        
        def helper(root, res):
            if not root:
                return
            for child in root.children:
                helper(child, res)
            res.append(root.val)
        
        helper(root, res)
        return res


# BFS
# Iterative
# runtime: faster than 57.57%
# https://blog.csdn.net/fuxuemingzhu/article/details/81017965
class Solution2:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            stack.extend(node.children)
            res.append(node.val)
        
        return res[::-1]