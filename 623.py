# 623. Add One Row to Tree
# Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS
# time: O(n)
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val, root, None)
            return node
        
        def dfs(node, curD, depth):
            if curD < depth -1:
                if node.left:
                    dfs(node.left, curD+1, depth)
                if node.right:
                    dfs(node.right, curD+1, depth)
            elif curD == depth -1:
                leftNode = TreeNode(val, node.left, None)
                rightNode = TreeNode(val, None, node.right)
                node.left = leftNode
                node.right = rightNode
                
            
        dfs(root, 1, depth)
        return root


# BFS
# time: O(n)
# https://leetcode.com/problems/add-one-row-to-tree/discuss/104582/Short-Python-BFS
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy, dummy.left = TreeNode(None), root
        row = [dummy]
        
        for _ in range(depth-1):
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        
        for node in row:
            node.left, node.left.left = TreeNode(val), node.left
            node.right, node.right.right = TreeNode(val), node.right
            
        return dummy.left


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)

        q = deque([root])
        d = 1
        while q and d <= depth - 1:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if d == depth - 1:
                    leftNode = TreeNode(val, cur.left, None)
                    rightNode = TreeNode(val, None, cur.right)
                    cur.left = leftNode
                    cur.right = rightNode
                else:
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
    
            d += 1
        
        return root