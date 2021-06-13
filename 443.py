# 443. String Compression
# String / Two Pointers

# runtime: O(n)
class Solution:
    def compress(self, chars: List[str]) -> int:
        pointer = 0
        i, j = 0, 0
        curr = chars[i]
        count = 0
        while j < len(chars):
            if chars[j] == curr:
                count += 1
                j += 1
            else:
                chars[pointer] = curr
                n = len(str(count)) if count > 1 else 0
                if n > 0:
                    chars[pointer+1: pointer+n+1] = list(str(count))
                pointer += n + 1
                i = j
                curr = chars[i]
                count = 0
        
        if count > 0:
            chars[pointer] = curr
            n = len(str(count)) if count > 1 else 0
            chars[pointer+1: pointer+n+1] = list(str(count))
            pointer += n + 1
        
        return pointer