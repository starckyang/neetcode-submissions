class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        x_space = [[0]*len(board[0]) for _ in range(len(board))]
        o_space = [[0]*len(board[0]) for _ in range(len(board))]

        def dfs(i, j, xo):
            directions = set([(i, j+1), (i, j-1), (i+1, j), (i-1, j)])
            if xo == "X":
                x_space[i][j]=1
                for dire in directions:
                    cur_i, cur_j = dire
                    if ((0<=cur_i<len(board)) and (0<=cur_j<len(board[0]))) and (board[cur_i][cur_j] == "X") and (x_space[cur_i][cur_j] == 0):
                        dfs(cur_i, cur_j, xo)
            else:
                o_space[i][j]=1
                for dire in directions:
                    cur_i, cur_j = dire
                    if ((0<=cur_i<len(board)) and (0<=cur_j<len(board[0]))) and (board[cur_i][cur_j] == "O") and (o_space[cur_i][cur_j] == 0):
                        dfs(cur_i, cur_j, xo)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0) or (i == (len(board)-1)) or (j == 0) or (j == (len(board[0])-1)):
                    if board[i][j] == "X":
                        dfs(i, j, "X")
                    else:
                        dfs(i, j, "O")

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    if x_space[i][j] == 0:
                        board[i][j] = "O"
                if board[i][j] == "O":
                    if o_space[i][j] == 0:
                        board[i][j] = "X"

        