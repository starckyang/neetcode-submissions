class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grids={i:{} for i in range(9)}
        rows={i:{} for i in range(9)}
        cols={i:{} for i in range(9)}

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                grid = (j//3) + (i//3)*3
                if ((num in rows[i]) or 
                    (num in cols[j]) or 
                    (num in grids[grid])):
                    return False
                
                rows[i][num]=True
                cols[j][num]=True
                grids[grid][num]=True

        return True