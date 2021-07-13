# 1186. Maximum Subarray Sum with One Deletion
# DP

# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/discuss/377424/Simple-Python-DP-solution
# runtime: O(n)
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        max_ending_0 = [arr[0]] * n
        max_ending_1 = [arr[0]] * n
        
        for i in range(1, n):
            max_ending_0[i] = max(max_ending_0[i-1]+arr[i], arr[i])
            max_ending_1[i] = max(max_ending_1[i-1]+arr[i], arr[i])
            if i >= 2:
                max_ending_1[i] = max(max_ending_1[i], max_ending_0[i-2]+arr[i])
        
        return max(max_ending_1)