# 290. Word Pattern
# Hash Table


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        mapping = {}
        visited = set()

        if len(pattern) != len(arr):
            return False
        
        for i,p in enumerate(pattern):
            if p in mapping:
                if mapping[p] != arr[i]:
                    return False
            elif arr[i] in visited:
                return False
            else:
                mapping[p] = arr[i]
                visited.add(arr[i])

        return True