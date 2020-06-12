# Spiral Matrix
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/79541501
# runtime: faster than 45.56%
class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        left, right, up, down = 0, n-1, 0, m-1
        res = []
        x, y = 0, 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_d = 0
        
        while len(res) != m*n:
            res.append(matrix[x][y])
            if cur_d == 0 and y == right:
                cur_d += 1
                up += 1
            elif cur_d == 1 and x == down:
                cur_d += 1
                right -= 1
            elif cur_d == 2 and y == left:
                cur_d += 1
                down -= 1
            elif cur_d == 3 and x == up:
                cur_d += 1
                left += 1
            
            cur_d %= 4
            x += dirs[cur_d][0]
            y += dirs[cur_d][1]
        
        return res


# runtime: faster than 98.22% 
class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        res = []
        self.x, self.y = 0, 0
        
        def spiral():
            move = False
            while self.y < n and not visited[self.x][self.y]:
                res.append(matrix[self.x][self.y])
                visited[self.x][self.y] = 1
                self.y += 1
                move = True
            
            self.y -= 1
            self.x += 1
            while self.x<m and not visited[self.x][self.y]:
                res.append(matrix[self.x][self.y])
                visited[self.x][self.y] = 1
                self.x += 1
                move = True
            
            self.x -= 1
            self.y -= 1
            while self.y >= 0 and not visited[self.x][self.y]:
                res.append(matrix[self.x][self.y])
                visited[self.x][self.y] = 1
                self.y -= 1
                move = True
            
            self.y += 1
            self.x -= 1
            while self.x >= 0 and not visited[self.x][self.y]:
                res.append(matrix[self.x][self.y])
                visited[self.x][self.y] = 1
                self.x -= 1
                move = True
            
            self.x += 1
            self.y += 1
            
            if move:
                spiral()
        
        spiral()
        return res