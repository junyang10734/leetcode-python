# Maximum Sum Circular Subarray
# Array

# https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/633550/Python-one-pass-solution-easy-to-understand
# runtime: faster than 65.41%
class Solution(object):
    def maxSubarraySumCircular(self, A):
        sub_max = A[0]    
        max_sum = A[0]
        sub_min = A[0]
        min_sum = A[0]
        total_sum = A[0]
        
	    # Get max & min subarray sum
        for num in A[1:]:
            total_sum += num
            
            sub_max = max(num, sub_max + num)
            sub_min = min(num, sub_min + num)
    
            max_sum = max(max_sum, sub_max)
            min_sum = min(min_sum, sub_min)
        
	    # Final max value should be max(total_sum - min_sum, max_sum)
	    # Consider subarray can't be empty, thus set the extra condition [>0] here
        if total_sum - min_sum > max_sum > 0:
            return total_sum - min_sum
        else:
            return max_sum