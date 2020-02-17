# Word Search

# https://leetcode.com/problems/word-search/discuss/429314/faster-(96)-low-memory(-100)-backtracking-python

# runtime: faster than 96.30%
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:        
        def backtrack(i, j, idx):
            s = board[i][j]
            if s != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            board[i][j] = ''
            
            if i>0 and backtrack(i-1,j,idx+1):
                return True
            if j>0 and backtrack(i,j-1,idx+1):
                return True
            if i<len(board)-1 and backtrack(i+1,j,idx+1):
                return True
            if j<len(board[0])-1 and backtrack(i,j+1,idx+1):
                return True
            board[i][j] = s      
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
            
        return False