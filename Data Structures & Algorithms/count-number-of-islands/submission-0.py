class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]

        def dfs(i, j):
            if not (0<=i<len(grid) and 0<=j<len(grid[0])):
                return
            if (grid[i][j] == "1") and (visited[i][j] != 1):
                visited[i][j] = 1
                dfs(i, j-1), dfs(i, j+1), dfs(i-1, j), dfs(i+1, j)

        islands=0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (visited[i][j] == 0) and (grid[i][j] == "1"):
                    islands+=1
                    dfs(i, j)

        return islands