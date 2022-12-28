# 1339. Maximum Product of Splitted Binary Tree
# Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# official sulotion
# 后序遍历
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []

        def getSum(subroot):
            if not subroot:
                return 0
            left_sum = getSum(subroot.left)
            right_sum = getSum(subroot.right)
            total_sum = subroot.val + left_sum + right_sum
            all_sums.append(total_sum)
            return total_sum

        total = getSum(root)
        res = 0
        for s in all_sums:
            res = max(res, s * (total - s))
        return res % (10 ** 9 + 7)
