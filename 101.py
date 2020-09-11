# Symmetric Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#  DaC, recursions
# faster than 63.86%
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isMirror(root.left,root.right)
    
    def isMirror(self, left, right) -> bool:
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)


# BFS, run lower
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        l = [root]
        length = 1
        while len(l)>0:
            for i in range(length):
                if l[i]:
                    l.append(l[i].left)
                    l.append(l[i].right)
                    if not l[length-i-1]:
                        return False
                    elif l[i].val != l[length-i-1].val:
                        return False
                else:
                    if l[length-i-1]:
                        return False
                    
            del l[:length]
            length = len(l)
            if length % 2 != 0:
                return False
        return True