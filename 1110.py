# 1110. Delete Nodes And Return Forest

# tree / recursive
# https://blog.csdn.net/Orientliu96/article/details/103219733


# running time: faster than 28.38%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        
        def helper(node, parent, loc):
            if not node:
                return
            if node.val in to_delete:
                if parent and loc == 1:
                    parent.left = None
                elif parent and loc == 2:
                    parent.right = None
                
                helper(node.left, None, 1)
                helper(node.right, None, 2)
            else:
                if not parent:
                    ans.append(node)
                helper(node.left, node, 1)
                helper(node.right, node, 2)

        helper(root, None, 0)
        
        return ans