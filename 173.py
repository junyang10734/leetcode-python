# Binary Search Tree Iterator
# Linked List

# BST
# runtime: faster than 67.17%
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.nodes_sorted = [] 
        self.index = -1
        self._inorder(root)
    
    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.nodes_sorted)


# Recursion
# runtime: faster than 12.07%
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftmost_inorder(root)
        
    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        topmost_node = self.stack.pop()
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# BST (inorder)
# https://blog.csdn.net/fuxuemingzhu/article/details/79436947
# Same as solution1, but with the descend order
# running time: faster than 5.10% 
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.inOrder(root)

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack) > 0
    
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.right)
        self.stack.append(root.val)
        self.inOrder(root.left)
