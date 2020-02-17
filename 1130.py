# Minimum Cost Tree From Leaf Values
# 该方法虽然可以计算出正确结果，但是Time Limit Exceeded
# 请参考贪心算法
class Solution1:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        def dp(i,j):
            if j <= i:
                return 0
            else:
                return min(dp(i,k-1) + dp(k,j) + max(arr[i:k])*max(arr[k:j+1]) for k in range(i+1,j+1))
        return dp(0,len(arr)-1)


# Minimum Cost Tree From Leaf Values
# Pick up the leaf node with minimum value.
# Combine it with its inorder neighbor which has smaller value between neighbors.
# Once we get the new generated non-leaf node, the node with minimum value is useless (For the new generated subtree will be represented with the largest leaf node value.)
# Repeat it until there is only one node.

class Solution2:
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