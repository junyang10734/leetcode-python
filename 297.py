# Serialize and Deserialize Binary Tree
# compare: 449, 428

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/399712/Python-strings-and-dictionary
# run time: faster than 36.27% 
class Codec1:

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



# https://blog.csdn.net/fuxuemingzhu/article/details/79571892
# faster than 56.55%
class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def preOrder(node):
            if not node:
                vals.append('#')
            else:
                vals.append(str(node.val))
                preOrder(node.left)
                preOrder(node.right)
        
        preOrder(root)
        return ' '.join(vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(val for val in data.split())
        def build():
            if vals:
                val = vals.popleft()
                if val == '#':
                    return None
                node = TreeNode(int(val))
                node.left = build()
                node.right = build()
                return node
        return build()


# https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485871&idx=1&sn=bcb24ea8927995b585629a8b9caeed01&chksm=9bd7f7a7aca07eb1b4c330382a4e0b916ef5a82ca48db28908ab16563e28a376b5ca6805bec2&scene=21#wechat_redirect
# 先序遍历
# runtime: faster than 0
class Codec3:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.s = ''
        def preOrder(node):
            self.s += ','
            if not node:
                self.s += '#'
            else:
                self.s += str(node.val)
                preOrder(node.left)
                preOrder(node.right)
        
        preOrder(root)
        
        return self.s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def flatten(nodes):
            if len(nodes) == 0:
                return None
                
            val = nodes.pop(0)
            if val == '#':
                return None

            root = TreeNode(int(val))
            root.left = flatten(nodes)
            root.right = flatten(nodes)
            
            return root
        
        return flatten(data.split(',')[1:])


# https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247485871&idx=1&sn=bcb24ea8927995b585629a8b9caeed01&chksm=9bd7f7a7aca07eb1b4c330382a4e0b916ef5a82ca48db28908ab16563e28a376b5ca6805bec2&scene=21#wechat_redirect
# 层级遍历
# runtime: faster than 81.78%
class Codec4:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 
        
        s = ''
        q = collections.deque()
        q.append(root)
        
        while q:
            node = q.popleft()    
            if not node:
                s += '#,'
                continue
            
            s += str(node.val)
            s += ','
            q.append(node.left)
            q.append(node.right)
            
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        nodes = data.split(',')[:-1]
        root = TreeNode(int(nodes[0]))
        q = collections.deque()
        q.append(root)
        
        i = 1
        while i < len(nodes):
            node = q.popleft()
            
            left = nodes[i]
            if left == '#':
                node.left = None
            else:
                leftNode = TreeNode(int(left))
                node.left = leftNode
                q.append(leftNode)
            i += 1
            
            right = nodes[i]
            if right == '#':
                node.right = None
            else:
                rightNode = TreeNode(int(right))
                node.right = rightNode
                q.append(rightNode)
            i += 1
              
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))