# Maximum Binary Tree
# Tree

# runtime: faster than 65.06%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        _max = max(nums)
        _max_pos = nums.index(_max)
        root = TreeNode(_max)
        root.left = self.constructMaximumBinaryTree(nums[:_max_pos])
        root.right = self.constructMaximumBinaryTree(nums[_max_pos+1:])
        
        return root 