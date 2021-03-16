# 863. All Nodes Distance K in Binary Tree
# DFS + BFS


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# https://blog.csdn.net/fuxuemingzhu/article/details/82709619
# runtime: faster than 52.33%
class Solution1:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # DFS
        d = collections.defaultdict(list)
        
        def connect(parent, child):
            if parent and child:
                d[parent.val].append(child.val)
                d[child.val].append(parent.val)
            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)
        
        connect(None, root)
        
        # BFS
        que = deque()
        que.append(target.val)
        seen =set([target.val])
        for k in range(K):
            size = len(que)
            for i in range(size):
                node = que.popleft()
                for j in d[node]:
                    if j not in seen:
                        que.append(j)
                        seen.add(j)
        return list(que)