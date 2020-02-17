# Partition Labels
'''
Intuition
Let's try to repeatedly choose the smallest left-justified partition. Consider the first label, say it's 'a'. The first partition must include it, and also the last occurrence of 'a'. However, between those two occurrences of 'a', there could be other labels that make the minimum size of this partition bigger. For example, in "abccaddbeffe", the minimum first partition is "abccaddb". This gives us the idea for the algorithm: For each letter encountered, process the last occurrence of that letter, extending the current partition [anchor, j] appropriately.

Algorithm
We need an array last[char] -> index of S where char occurs last. Then, let anchor and j be the start and end of the current partition. If we are at a label that occurs last at some index after j, we'll extend the partition j = last[c]. If we are at the end of the partition (i == j) then we'll append a partition size to our answer, and set the start of our new partition to i+1.
'''

class Solution:
    def partitionLabels(self, S: str) -> List[int]:        
        last = {c: i for i,c in enumerate(S)}
        start = end = 0
        ans = []
        for i,c in enumerate(S):
            end = max(end, last[c])
            if i == end:
                ans.append(i-start+1)
                start = i + 1
        return ans  