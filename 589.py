# N-ary Tree Preorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Recursive
# runtime: faster than 91.18%
# https://zxi.mytechroad.com/blog/tree/leetcode-589-n-ary-tree-preorder-traversal/
class Solution1:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
    
        res = []
        def order(node):
            res.append(node.val)
            for child in node.children:
                order(child)
        
        order(root)
        return res


# runtime: faster than 56.91%
# https://blog.csdn.net/fuxuemingzhu/article/details/81021950
class Solution1:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
    
        ans = []
        ans.append(root.val)
        for child in root.children:
            ans.extend(self.preorder(child))
        
        return ans


# Iterative
# runtime: faster than 56.91%
# https://blog.csdn.net/fuxuemingzhu/article/details/81021950
class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        ans = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children[::-1])
        
        return ans 