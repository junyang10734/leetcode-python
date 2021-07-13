# Symmetric Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursive
# runtime: O(n)
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


# iteration
# runtime: O(n)
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = collections.deque()
        q.append((root.left, root.right))
        while q:
            node1, node2 = q.popleft()
            if not node1 and not node2:
                continue
            elif (not node1 or not node2) or node1.val != node2.val:
                return False
            else:
                q.append((node1.left, node2.right))
                q.append((node1.right, node2.left))
        return True