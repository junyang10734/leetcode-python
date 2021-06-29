# 473. Matchsticks to Square
# DFS

# https://leetcode.com/problems/matchsticks-to-square/solution/

# DFS
# runtims: O(4**n)
class Solution1:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        total = sum(matchsticks)
        if n == 0 or total % 4 != 0:
            return False
        
        side_length = total // 4
        matchsticks.sort(reverse=True)
        sides = [0 for _ in range(4)]
        
        def dfs(index):
            if index == n:
                return sides[0] == sides[1] == sides[2] == side_length
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= side_length:
                    sides[i] += matchsticks[index]
                    if dfs(index+1):
                        return True
                    sides[i] -= matchsticks[index]
            
            return False                    

        return dfs(0)
