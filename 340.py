# 340. Longest Substring with At Most K Distinct Characters
# sliding window

# runtime: O(n)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        maxSize = 0
        counter = collections.Counter()

        left = 0
        for right in range(n):
            counter[s[right]] += 1

            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            maxSize = max(maxSize, right - left + 1)
        
        return maxSize
    
    
# runtime: O(n)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        cnt = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            char = s[r]
            if char in cnt:
                cnt[char] += 1
                r += 1
            else:
                cnt[char] = 1
                if len(cnt) > k:
                    res = max(res, r-l)
                    while l <= r and len(cnt) > k:
                        char = s[l]
                        if cnt[char] == 1:
                            del cnt[char]
                        else:
                            cnt[char] -= 1
                        l += 1
                r += 1
    
        return max(res, r-l)        