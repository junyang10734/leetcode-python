# Balanced Binary Tree
# Tree

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://www.cnblogs.com/zuoyuan/p/3720169.html
# runtime: faster than 26.49%
class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    def getHeight(self, root):
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1


# https://zxi.mytechroad.com/blog/leetcode/leetcode-110-balanced-binary-tree/
# faster than 77.66% 
class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        self.balance = True
        
        def height(root):
            if not root or not self.balance:
                return -1
            l = height(root.left)
            r = height(root.right)
            if abs(l - r) > 1:
                self.balance = False
                return -1
            
            return max(l, r) + 1
        
        height(root)
        return self.balance
