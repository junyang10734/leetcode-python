# Queue Reconstruction by Height
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if len(people) == 0:
            return []
        
        people.sort(key=lambda x:(-x[0],x[1]))
        ans = []
        for p in people:
            ans.insert(p[1],p)
        return ans