# Path Sum

# https://blog.csdn.net/fuxuemingzhu/article/details/71715810

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# recursive
# faster than 15.28% 
class Solution1:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


# BFS
# faster than 26.71%
class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        q = collections.deque()
        q.append((root, root.val))
        
        while q:
            node, path = q.popleft()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                q.append((node.left, path + node.left.val))
            if node.right:
                q.append((node.right, path + node.right.val))
        return False


# backtrack / DFS
# faster than 73.80%
class Solution3:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        def dfs(node, total):
            nonlocal targetSum

            total += node.val
            if total == targetSum and not node.left and not node.right:
                return True
            
            left, right = False, False
            if node.left:
                left = dfs(node.left, total)
            if node.right:
                right = dfs(node.right, total)
            return left or right
        
        return dfs(root, 0)


# stack
# faster than 97.32% 
class Solution4:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = []
        stack.append((root, root.val))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                stack.append((node.left, path + node.left.val))
            if node.right:
                stack.append((node.right, path + node.right.val))
        return False