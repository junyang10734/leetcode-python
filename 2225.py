# 2225. Find Players With Zero or One Losses
# Hash Table

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        for winer, loser in matches:
            if winer in d:
                d[winer][0] += 1
            else:
                d[winer] = [1, 0]
                
            if loser in d:
                d[loser][1] += 1
            else:
                d[loser] = [0, 1]  
        
        arr1, arr2 = [], []
        for k, v in d.items():
            if v[1] == 0:
                arr1.append(k)
            elif v[1] == 1:
                arr2.append(k)

        return [sorted(arr1), sorted(arr2)]