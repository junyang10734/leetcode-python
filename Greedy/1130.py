# Minimum Cost Tree From Leaf Values
# Pick up the leaf node with minimum value.
# Combine it with its inorder neighbor which has smaller value between neighbors.
# Once we get the new generated non-leaf node, the node with minimum value is useless (For the new generated subtree will be represented with the largest leaf node value.)
# Repeat it until there is only one node.

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        
        while len(arr) > 1:
            idx = arr.index(min(arr))
            
            if idx == 0:
                res += arr[1]*arr[idx]
            elif idx == len(arr)-1:
                res += arr[idx-1]*arr[idx]
            else:
                res += min(arr[idx-1], arr[idx+1]) * arr[idx]
            
            arr.pop(idx)
        
        return res