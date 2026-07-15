class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = [[0]*len(heights[0]) for _ in range(len(heights))]
        atlantic = [[0]*len(heights[0]) for _ in range(len(heights))]

        def dfs(i, j, visited):
            visited[i][j] = 1
            for direction in set([(i, j+1), (i, j-1), (i+1, j), (i-1, j)]):
                ci, cj = direction
                if (0<=ci<len(heights)) and (0<=cj<len(heights[0])) and (visited[ci][cj] == 0):
                    if heights[i][j] <= heights[ci][cj]:
                        dfs(ci, cj, visited)

        for i in range(len(heights)):
            dfs(i, 0, pacific)     
            dfs(i, len(heights[0])-1, atlantic)            

        for j in range(len(heights[0])):
            dfs(0, j, pacific)     
            dfs(len(heights)-1, j, atlantic)  

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if atlantic[i][j] == 1 and pacific[i][j] == 1:
                    res.append((i,j))

        return res
        