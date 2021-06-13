# 1152. Analyze User Website Visit Pattern
# Hash Table

# https://leetcode.com/problems/analyze-user-website-visit-pattern/discuss/355388/Python-Solution
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = zip(timestamp, username, website)
        sorted_visits = sorted(visits)
        mapping = collections.defaultdict(list)
        for t,u,w in sorted_visits:
            mapping[u].append(w)
        
        counter = collections.defaultdict(int)
        for ws in mapping.values():
            combs = set(itertools.combinations(ws, 3))
            for comb in combs:
                counter[comb] += 1
        
        sorted_counter = sorted(counter, key=lambda x:(-counter[x], x))
        return sorted_counter[0]
