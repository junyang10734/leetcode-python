# Count Servers that Communicate
# Array / Graph

# runtime: faster than 43.34%
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        nums = 0
        label = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        for i in range(len(grid)):
            l = grid[i]
            if l.count(1) > 1:  
                for idx, item in enumerate(l):
                    if item == 1 and label[i][idx] == 0:
                        label[i][idx] = 1
                        nums += 1
        
        
        for j in range(len(grid[0])):
            nums1 = 0
            nums2 = 0
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    nums1 += 1
                    if label[i][j] == 0:
                        nums2 += 1
                        label[i][j] = 1
            if nums1 > 1:
                nums += nums2
        
        return nums  