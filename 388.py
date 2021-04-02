# 388. Longest Absolute File Path
# String

# https://leetcode.com/problems/longest-absolute-file-path/discuss/86619/Simple-Python-solution
# runtime: faster than 76.43%
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        res = 0
        path = {0: 0}
        print(input.split('\n'))
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                res = max(res, path[depth] + len(name))
            else:
                path[depth+1] = path[depth] + len(name) + 1
        return res