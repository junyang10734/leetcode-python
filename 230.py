# Kth Smallest Element in a BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# inorder traverse
# recursion
# runtime: faster than 67.63%
class Solution1:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return inorder(root)[k-1]


# iteration
# runtime: faster than 99.85%
class Solution2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


class Solution3:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        self.num = 0
        def traverse(node, k):
            if not node:
                return
            traverse(node.left, k)
            self.num += 1
            if self.num == k:
                self.res = node.val
                return
            traverse(node.right, k)
        
        traverse(root, k)
        return self.res