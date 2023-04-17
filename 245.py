# 245. Shortest Word Distance III
# Array

# time: O(n)
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        ans = n
        same = word1 == word2
        last_seen_idx = None

        for i in range(n):
            if wordsDict[i] == word1 or wordsDict[i] == word2:
                if last_seen_idx != None:
                    if same or wordsDict[last_seen_idx] != wordsDict[i]:
                        ans = min(ans, i - last_seen_idx)
                last_seen_idx = i
        return ans
