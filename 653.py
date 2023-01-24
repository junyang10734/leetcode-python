# 653. Two Sum IV - Input is a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# HashTable
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()

        def helper(node):
            nonlocal k
            if not node:
                return False
            if (k - node.val) in s:
                return True
            s.add(node.val)
            return helper(node.left) or helper(node.right)
        
        return helper(root)


# BFS + HashTable
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node:
                val = node.val
                if (k - val) in s:
                    return True
                s.add(val)
                queue.append(node.left)
                queue.append(node.right)
        
        return False