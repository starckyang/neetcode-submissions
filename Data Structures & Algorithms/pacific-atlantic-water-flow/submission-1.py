class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = [[0]*len(heights[0]) for _ in range(len(heights))]
        atlantic = [[0]*len(heights[0]) for _ in range(len(heights))]

        def dfs(i, j, c_type, visited=[[0]*len(heights[0]) for _ in range(len(heights))]):
            """
            if c_type = 0, pacific, c_types = 1, atlantic, c_type = 2, both
            """
            if c_type == 0:
                pacific[i][j] = 1
                for direction in set([(i, j+1), (i, j-1), (i+1, j), (i-1, j)]):
                    ci, cj = direction
                    if (0<=ci<len(heights)) and (0<=cj<len(heights[0])) and (pacific[ci][cj] == 0):
                        if heights[i][j] <= heights[ci][cj]:
                            dfs(ci, cj, c_type)

            elif c_type == 1:
                atlantic[i][j] = 1
                for direction in set([(i, j+1), (i, j-1), (i+1, j), (i-1, j)]):
                    ci, cj = direction
                    if (0<=ci<len(heights)) and (0<=cj<len(heights[0])) and (atlantic[ci][cj] == 0):
                        if heights[i][j] <= heights[ci][cj]:
                            dfs(ci, cj, c_type)

            else:
                atlantic[i][j] = 1
                pacific[i][j] = 1
                for direction in set([(i, j+1), (i, j-1), (i+1, j), (i-1, j)]):
                    ci, cj = direction
                    if (0<=ci<len(heights)) and (0<=cj<len(heights[0])) and ((atlantic[ci][cj] == 0) or (pacific[ci][cj] == 0)):
                        if heights[i][j] <= heights[ci][cj]:
                            dfs(ci, cj, c_type)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if ((i, j) == (0, len(heights[0])-1)) or ((i, j) == (len(heights)-1, 0)):
                    ctype=2
                elif (i == 0) or (j==0):
                    ctype=0
                elif (i==len(heights)-1) or (j==len(heights[0])-1):
                    ctype=1
                else:
                    continue
                dfs(i, j, ctype)

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if atlantic[i][j] == 1 and pacific[i][j] == 1:
                    res.append((i,j))

        return res
        