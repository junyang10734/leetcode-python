# 109. Convert Sorted List to Binary Search Tree
# Same as 108

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# https://blog.csdn.net/fuxuemingzhu/article/details/80785093
# 先转化为数组，然后构建BST
# runtime: faster than 45.70%
class Solution1:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        return self.helper(nums)
        
    
    def helper(self, nums):
        if not nums:
            return None
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums[:mid])
        node.right = self.helper(nums[mid+1:])
        return node


# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solution/
# Inorder Simulation
# runtime: faster than 77.99%
class Solution2:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        N = self.findSize(head)
        
        def buildTree(l, r):
            if l > r:
                return None
            
            nonlocal head
            mid = (l+r)//2
            left = buildTree(l, mid-1)
            node = TreeNode(head.val)
            node.left = left
            
            head = head.next
            node.right = buildTree(mid+1, r)
            
            return node
        
        return buildTree(0, N-1)
       
    def findSize(self, head):
        node = head
        c = 0
        while node:
            c += 1
            node = node.next
        return c 
