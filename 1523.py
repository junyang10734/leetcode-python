# 1523. Count Odd Numbers in an Interval Range
# math

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2