# 1086. High Five
# Array / Hash Table / Sort

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = collections.defaultdict(list)
        for idx, score in items:
            scores[idx].append(score)
        
        res = []
        for k,v in scores.items():
            res.append([k, sum(sorted(v, key=lambda x: -x)[:5]) // 5])
        return sorted(res)