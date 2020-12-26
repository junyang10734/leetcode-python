# 659. Split Array into Consecutive Subsequences
# greedy

# https://leetcode.com/problems/split-array-into-consecutive-subsequences/solution/
# running time: faster than 44.14% 
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        tails = collections.Counter()

        for n in nums:
            if count[n] == 0:
                continue
            elif tails[n] > 0:
                tails[n] -= 1
                tails[n+1] += 1
            elif count[n+1] > 0 and count[n+2] > 0:
                count[n+1] -= 1
                count[n+2] -= 1
                tails[n+3] += 1
            else:
                return False
            count[n] -= 1
        return True