# Most Frequent Subtree Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursion
# https://blog.csdn.net/fuxuemingzhu/article/details/79435381
# faster than 35.64%
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        vals = []
        
        def getSum(node):
            if not node:
                return 0
            s = getSum(node.left) + node.val + getSum(node.right)
            vals.append(s)
            return s
        
        getSum(root)
        count = collections.Counter(vals)
        frequent = max(count.values())
        return [x for x,v in count.items() if v == frequent]