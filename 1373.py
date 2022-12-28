# 1373. Maximum Sum BST in Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# labuladong
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum = 0
        self.traverse(root)
        return self.maxSum
    
    def traverse(self, node):
        if not node:
            return [1, math.inf, -math.inf, 0]
        
        left = self.traverse(node.left)
        right = self.traverse(node.right)

        res = [0, math.inf, -math.inf, 0] # [isBST, minV of BST, maxV of BST, sum of BST]
        if left[0] and right[0]: # both left subtree and right subtree are BST
            if node.val > left[2] and node.val < right[1]: # the tree with node as root is BST
                res[0] = 1
                res[1] = min(left[1], node.val)
                res[2] = max(right[2], node.val)
                res[3] = left[3] + right[3] + node.val
                self.maxSum = max(self.maxSum, res[3])

        return res