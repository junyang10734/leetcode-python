# Binary Tree Cameras

# DP
# faster than 20.11%
class Solution1:
    def minCameraCover(self, root: TreeNode) -> int:
        def dp(node):
            if not node:
                return 0, 0, float('inf')
            L = dp(node.left)
            R = dp(node.right)
            
            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)
            
            return dp0, dp1, dp2
        
        return min(dp(root)[1:])


# Greedy
# faster than 80.65%
class Solution2:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        covered = {None}
        
        def dfs(node, par=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                
                if(not par and node not in covered or node.left not in covered or node.right not in covered):
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})
        
        dfs(root)
        return self.ans 