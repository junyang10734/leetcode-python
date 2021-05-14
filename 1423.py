# 1423. Maximum Points You Can Obtain from Cards
# Sliding Window

# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/solution/
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597763/Python3-Easy-Sliding-Window-O(n)%3A-Find-minimum-subarray
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        subArraySum = inf
        j = curr = 0
        
        for i,v in enumerate(cardPoints):
            curr += v
            if i - j + 1 > size:
                curr -= cardPoints[j]
                j += 1
            if i - j + 1 == size:
                subArraySum = min(subArraySum, curr)

        
        return sum(cardPoints) - subArraySum
