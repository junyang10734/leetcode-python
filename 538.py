# 538. Convert BST to Greater Tree
# Tree 
# same as 1038

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 后续遍历 + 维护一个sum值
# runtime: faster than 8.61%
class Solution1:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.s = 0
        
        def postOrder(node):
            if not node:
                return 
            postOrder(node.right)
            self.s += node.val
            node.val = self.s
            postOrder(node.left)
            
        postOrder(root)
        return root


# runtime: faster than 85%
class Solution2:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        arr = []
        
        def dfs(node):
            arr.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        
        arr.sort()
        d = collections.defaultdict(int)
        d[arr[-1]] = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            d[arr[i]] = d[arr[i+1]] + arr[i]
        
        
        def dfs2(node):
            node.val = d[node.val]
            if node.left:
                dfs2(node.left)
            if node.right:
                dfs2(node.right)
        dfs2(root)
        
        return root
        

# https://leetcode.com/problems/convert-bst-to-greater-tree/discuss/100555/Python-Simple-with-Explanation
# runtime: faster than 96%
class Solution3:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.val = 0
        def dfs(node):
            if node:
                dfs(node.right)
                node.val += self.val
                self.val = node.val
                dfs(node.left)
        dfs(root)
        return root