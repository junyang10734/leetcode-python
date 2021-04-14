# Serialize and Deserialize BST
# compare: 297, 428

# https://blog.csdn.net/fuxuemingzhu/article/details/79529337


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/serialize-and-deserialize-bst/solution/
# preOrder
# runtime: faster than 62.40%, O(n)
class Codec1:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def preOrder(root):
            return [root.val] + preOrder(root.left) + preOrder(root.right) if root else []
        return ' '.join(map(str, preOrder(root)))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = [int(x) for x in data.split(' ') if x]
        def helper(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] < lower or data[0] > upper:
                return
            val = data.pop(0)
            root = TreeNode(int(val))
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root
        return helper()


# preOder template, for all bianary tree
# DFS
# runtime: faster than 5.35%
class Codec2:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        self.s = ''
        def preOrder(node):
            if not node:
                self.s += '#,'
            else:
                self.s += str(node.val)
                self.s += ','
                preOrder(node.left)
                preOrder(node.right)
        preOrder(root)
        return self.s
                
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def flatten(nodes):
            if len(nodes) == 0:
                return
            val = nodes.pop(0)
            if val == '#':
                return
            root = TreeNode(int(val))
            root.left = flatten(nodes)
            root.right = flatten(nodes)
            return root
        return flatten(data.split(','))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))