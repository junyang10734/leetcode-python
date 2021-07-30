# 744. Find Smallest Letter Greater Than Target
# Binary Search

# runtime: O(logn)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]