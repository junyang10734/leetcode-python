# Binary Tree Paths

# https://blog.csdn.net/fuxuemingzhu/article/details/71249429

# DFS + Recursion
# faster than 51.17%
class Solution1:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        res = []
        self.dfs(root, res, str(root.val))
        return res
    
    def dfs(self, node, res, path):
        if not node.left and not node.right:
            res.append(path)
        if node.left:
            self.dfs(node.left, res, path + '->' + str(node.left.val))
        if node.right:
            self.dfs(node.right, res, path + '->' + str(node.right.val))


# Iteration + Stack
# faster than 75.00%
class Solution2:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        res = []
        stack = []
        stack.append((root, str(root.val)))
        
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        
        return res