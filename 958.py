# 958. Check Completeness of a Binary Tree

# https://blog.csdn.net/fuxuemingzhu/article/details/85032299
# DFS
# runtime: faster than 26.55%  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        res = []
        self.getLevel(res, 0, root)
        depth = len(res)-1
        
        for d in range(depth):
            if d != depth -1:
                if None in res[d] or len(res[d])!= (2**d):
                    return False
            else:
                ni = -1
                for i, n in enumerate(res[d]):
                    if not n:
                        if ni == -1:
                            ni = i
                    else:
                        if ni != -1:
                            return False
                
        return True
    
    def getLevel(self, res, level, node):
        if level >= len(res):
            res.append([])
            
        if not node:
            res[level].append(None)
        else:
            res[level].append(node.val)
            self.getLevel(res, level+1, node.left)
            self.getLevel(res, level+1, node.right)