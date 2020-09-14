# Binary Tree Level Order Traversal II
# Tree / DFS

# https://blog.csdn.net/fuxuemingzhu/article/details/49108449

# DFS
# runtime: faster than 11.78%
class Solution1:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.levelOrder(root, res, 0)
        return res[::-1]

    def levelOrder(self, root, res, level):
        if not root:
            return 
        if level >= len(res):
            res.append([])
        res[level].append(root.val)
        self.levelOrder(root.left, res, level + 1)
        self.levelOrder(root.right, res, level + 1)


# BFS
# faster than 43.70%  
class Solution2:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []
            size = len(q)
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        
        return res[::-1]


# Iteration
# runtime: faster than 7.08%
class Solution3:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        que = collections.deque()
        que.append(root)
        level = 0
        
        while que:
            levelVal = []
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if not node:
                    continue
                levelVal.append(node.val)
                que.append(node.left)
                que.append(node.right)
            level += 1
            if levelVal:
                res.append(levelVal)
        return res[::-1]
