class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        used = [[False] * n for _ in range(m)]

        def dfs(i, r, c):
            if not (0 <= r < m and 0 <= c < n):
                return False

            if used[r][c] or board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            used[r][c] = True

            found = (
                dfs(i + 1, r + 1, c) or
                dfs(i + 1, r - 1, c) or
                dfs(i + 1, r, c + 1) or
                dfs(i + 1, r, c - 1)
            )

            used[r][c] = False
            return found

        for r in range(m):
            for c in range(n):
                if dfs(0, r, c):
                    return True

        return False