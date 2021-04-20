# Reverse Words in a String
# String

# runtime: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        res = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i] != '':
                res.append(arr[i])
        return ' '.join(res)

# runtime: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))