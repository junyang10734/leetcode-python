# 117. Populating Next Right Pointers in Each Node II
# Tree / BFS

# https://blog.csdn.net/fuxuemingzhu/article/details/79560379
# running time: faster than 9.75%
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        que = collections.deque()
        que.append(root)
        
        while que:
            N = len(que)
            for i in range(N):
                node = que.popleft()
                if i < N-1:
                    node.next = que[0]
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        
        return root
