# 937. Reorder Data in Log Files
# String

# https://leetcode.com/problems/reorder-data-in-log-files/solution/
# Sorting by key
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def get_key(log):
            _id, text = log.split(' ', maxsplit=1)
            return (0, text, _id) if text[0].isalpha() else (1, )
            
        return sorted(logs, key=get_key)