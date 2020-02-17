# Serialize and Deserialize Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/399712/Python-strings-and-dictionary
# run time: faster than 36.27% 
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree = {}
        def process(root, key):
            if not root: return
            tree[key] = root.val
            
            process(root.left, key+'0')
            process(root.right, key+'1')
        
        process(root, '')
        return str(tree)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = eval(data)
        def process(key):
            if key not in tree: return
            
            node = TreeNode(tree[key])
            node.left = process(key+'0')
            node.right = process(key+'1')
            
            return node
        
        return process('')


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))