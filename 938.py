# 938. Range Sum of BST
# Tree / DFS

# https://leetcode.com/problems/range-sum-of-bst/solution/
# runtime: O(n)
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.res = 0
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.res += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
        
        dfs(root)
        return self.res