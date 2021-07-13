# Binary Tree Level Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS
# runtime: O(n)
class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        def dfs(node, depth):
            if len(res) <= depth:
                res.append([])
            
            res[depth].append(node.val)
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
        
        if root:
            dfs(root, 0)
        
        return res


# BFS
# runtime: O(n)
class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)
        
        while q:
            size = len(q)
            arr = []
            for i in range(size):
                node = q.popleft()
                arr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(arr)
        return res