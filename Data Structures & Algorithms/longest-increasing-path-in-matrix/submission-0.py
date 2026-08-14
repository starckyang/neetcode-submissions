class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        memo={}
        
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            directions=[(i, j-1), (i, j+1), (i+1, j), (i-1, j)]
            ans=1
            for dir in directions:
                ni, nj=dir[0], dir[1]
                if 0<=ni<len(matrix) and 0<=nj<len(matrix[0]):
                    if matrix[i][j] < matrix[ni][nj]:
                        ans=max(ans, 1+dfs(ni,nj))
            memo[(i,j)]=ans
            return ans

        res=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res=max(res, dfs(i,j))

        return res

