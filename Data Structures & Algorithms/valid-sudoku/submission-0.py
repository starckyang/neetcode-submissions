class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        clusters = {i: {} for i in range(27)}
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if (num in clusters[i]) or (num in clusters[9+j]) or (num in clusters[18 + (i//3) * 3 + (j//3)]):
                    return False
                clusters[i][num] = True
                clusters[9+j][num] = True
                clusters[18 + (i//3) * 3 + (j//3)][num] = True
        return True