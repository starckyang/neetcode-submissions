class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # we need n(row) + n(col) + (2n-1) (right diag) + (2n-1) (left diag)

        res = []
        def dfs(r=0, board=[], diag=[0]*(2*n-1), rev_diag=[0]*(2*n-1), cols=[0]*n):
            if r >= n:
                res.append(board.copy())
                return
            for i in range(n):
                if cols[i] == 1:
                    pass
                else:
                    if (diag[(i-r+n-1)] == 0) and (rev_diag[(r+i)] == 0):
                        line = "." * i + "Q" + "." * (n-i-1)
                        board.append(line)
                        diag[(i-r+n-1)]=1
                        rev_diag[(r+i)]=1
                        cols[i]=1
                        dfs(r+1, board, diag, rev_diag, cols)
                        board.pop()
                        diag[(i-r+n-1)]=0
                        rev_diag[(r+i)]=0
                        cols[i]=0

        dfs()
        return res

