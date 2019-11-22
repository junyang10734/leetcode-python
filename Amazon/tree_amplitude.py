"""
Given a tree of N nodes, return the amplitude of the tree.
就是从 root 到 leaf max - min 的差
"""


# definition of TreeNode
class TreeNode:
    def __index__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def treeAmplitude(self, root):
        if root is None:
            return 0
        return self.helper(root, root.val, root.val)

    def helper(self, node, min_val, max_val):
        if node is None:
            return max_val - min_val

        if node.val < min_val:
            min_val = node.val
        if node.val > max_val:
            max_val = node.val

        return max(self.helper(node.left, min_val, max_val), self.helper(node.right, min_val, max_val))
