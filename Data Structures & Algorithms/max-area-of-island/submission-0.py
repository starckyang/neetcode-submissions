class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]

        def dfs(i, j):
            if not (0<=i<len(grid) and 0<=j<len(grid[0])):
                return 0
            if (visited[i][j] == 1) or (grid[i][j] == 0):
                return 0
            visited[i][j] = 1
            return 1 + sum([dfs(i, j-1), dfs(i, j+1), dfs(i-1, j), dfs(i+1, j)])

        marea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1) and (visited[i][j] != 1):
                    area = dfs(i, j)
                    marea = area if area > marea else marea

        return marea