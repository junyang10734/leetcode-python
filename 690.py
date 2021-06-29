# 690. Employee Importance
# Hash Table / DFS

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# https://leetcode.com/problems/employee-importance/solution/
# runtime: O(n)
class Solution1:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {e.id: e for e in employees}
        
        def dfs(eid):
            e = d[eid]
            return e.importance + sum(dfs(idx) for idx in e.subordinates)
        
        return dfs(id)


# runtime: O(n)
class Solution2:
    def getImportance(self, employees: List['Employee'], id: int) -> int:        
        res = 0
        idx = 0
        sub = []
        d = {}
        
        for i,e in enumerate(employees):
            if e.id == id:
                res += e.importance
                sub = e.subordinates
                idx = i + 1
                break
            else:
                d[e.id] = e

        
        for s in sub:
            if s in d:
                res += d[s].importance
                sub += d[s].subordinates
            else:
                while idx < len(employees):
                    e = employees[idx]
                    if e.id == s:
                        res += e.importance
                        idx += 1
                        sub += e.subordinates
                        break
                    else:
                        d[e.id] = e
                        idx += 1
        
        return res
        
        
        
