# Path Sum III
# Tree

# https://blog.csdn.net/fuxuemingzhu/article/details/71097135

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS + DFS
# runtime: faster than 32.80% 
class Solution1:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
    
    def dfs(self, root, sum):
        res = 0
        if not root:
            return res
        
        sum -= root.val
        if sum == 0:
            res += 1
        res += self.dfs(root.left, sum)
        res += self.dfs(root.right, sum)
        
        return res


# DFS + BFS
# runtime: faster than 30.11%
class Solution2:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        res = [0]
        que = collections.deque()
        que.append(root)
        while que:
            node = que.popleft()
            if not node:
                continue
            self.dfs(node, res, 0, sum)
            que.append(node.left)
            que.append(node.right)
        return res[0]
    
    
    def dfs(self, root, res, path, target):
        if not root:
            return
        path += root.val
        if path == target:
            res[0] += 1
        self.dfs(root.left, res, path, target)
        self.dfs(root.right, res, path, target)
