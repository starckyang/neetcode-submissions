import math
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        
        def dfs(i, j, dist=0):
            if not ((0<=i<len(grid)) and (0<=j<len(grid[0]))):
                return
            if (grid[i][j] == -1) or (dist > grid[i][j]):
                return
            grid[i][j] = dist if dist < grid[i][j] else grid[i][j]
            dfs(i, j+1, dist=dist+1), dfs(i, j-1, dist=dist+1), dfs(i+1, j, dist=dist+1), dfs(i-1, j, dist=dist+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(i, j, dist=0)
            