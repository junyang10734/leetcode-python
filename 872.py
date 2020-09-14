# Leaf-Similar Trees
# https://blog.csdn.net/fuxuemingzhu/article/details/81748617


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# preOrder
# Recursion
# faster than 10.83%
class Solution1:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.getLeaves(root1) == self.getLeaves(root2)
    
    def getLeaves(self, node):
        res = []
        if not node:
            return res
        if not node.left and not node.right:
            return [node.val]
        res.extend(self.getLeaves(node.left))
        res.extend(self.getLeaves(node.right))
        return res

# Iteration
# faster than 23.39%
class Solution1:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.preOrder(root1) == self.preOrder(root2)
        
    def preOrder(self, root):
        stack = []
        stack.append(root)
        res = []
        
        while stack:
            node = stack.pop()
            if not node:
                continue
            if not node.left and not node.right:
                res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        
        return res



# inOrder
# faster than 18.27%
class Solution2:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1, l2 = [], []
        self.inOrder(root1, l1)
        self.inOrder(root2, l2)
        return l1 == l2
    
    def inOrder(self, node, l):
        if not node:
            return
        self.inOrder(node.left, l)
        if not node.left and not node.right:
            l.append(node.val)
        self.inOrder(node.right, l)



# postOrder
# faster than 99.56%
class Solution3:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.postOrder(root1) == self.postOrder(root2)
    
    def postOrder(self, root):
        stack = []
        stack.append(root)
        res = []
        
        while stack:
            node = stack.pop()
            if not node:
                continue
            stack.append(node.left)
            stack.append(node.right)
            if not node.left and not node.right:
                res.append(node.val)
        
        return res