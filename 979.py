# Distribute Coins in Binary Tree

# https://leetcode.com/problems/distribute-coins-in-binary-tree/solution/
# DFS + Recursion
# faster than 79.35%
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1
        
        dfs(root)
        return self.ans