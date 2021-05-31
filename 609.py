# 609. Find Duplicate File in System
# String

# https://leetcode.com/problems/find-duplicate-file-in-system/discuss/104122/Python-Straightforward-with-Explanation
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for line in paths:
            p = line.split()
            root = p[0]
            for file in p[1:]:
                name, _, content = file.partition('(')
                d[content[:-1]].append(root + '/' + name)
        return [x for x in d.values() if len(x) > 1]
