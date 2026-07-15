import math
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def bfs(i, j):
            queue = deque([(i, j)])
            visited = [[0]*len(grid[0]) for _ in range(len(grid))]
            dist = -1
            while queue:
                dist += 1
                round_cnt = len(queue)
                for cnt in range(round_cnt):
                    y, x = queue.popleft()
                    if not ((0<=y<len(grid)) and (0<=x<len(grid[0]))):
                        continue
                    if (visited[y][x] == 1) or ((grid[y][x]==0) and (dist!=0)) or (grid[y][x]==-1):
                        continue
                    if grid[y][x] < dist:
                        continue
                    visited[y][x] = 1
                    grid[y][x] = dist
                    queue.extend([(y, x-1), (y, x+1), (y+1, x), (y-1, x)])
            return dist-1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = math.inf
                elif grid[i][j] == 2:
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1 


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs(i, j)
    
        max_dist = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_dist = max_dist if grid[i][j] < max_dist else grid[i][j]
                if grid[i][j] == math.inf:
                    return -1

        return max_dist