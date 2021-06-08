# 424. Longest Repeating Character Replacement
# sliding window

# https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91301/Awesome-python-solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter()
        start, res = 0, 0
        for end in range(len(s)):
            cnt[s[end]] += 1
            max_count = cnt.most_common(1)[0][1]
            if end - start + 1 - max_count > k:
                cnt[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        return res
