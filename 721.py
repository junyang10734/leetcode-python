# 721. Accounts Merge
# Graph
# https://leetcode.com/problems/accounts-merge/solution/


# DFS
# runtime: faster than 97.94%
class Solution1:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = collections.defaultdict(set)
        for a in accounts:
            name = a[0]
            for email in a[1:]:
                graph[a[1]].add(email)
                graph[email].add(a[1])
                email_to_name[email] = name
        
        seen = set()
        res = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                res.append([email_to_name[email]] + sorted(component))
        
        return res   


# Union-Find
# runtime: faster than 53.88%
class DSU:
    def __init__(self):
        self.parent = list(range(10001))
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        em_name, em_id = {}, {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_name[email] = name
                if email not in em_id:
                    em_id[email] = i
                    i += 1
                dsu.union(em_id[acc[1]], em_id[email])
        
        res = collections.defaultdict(list)
        for email in em_name:
            res[dsu.find(em_id[email])].append(email)
        
        return [[em_name[v[0]]] + sorted(v) for v in res.values()]      