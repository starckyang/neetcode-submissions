class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(comb="", open=n, close=n):
            if (open < 0) or (close < 0) or (close < open):
                return
            if open == close == 0:
                res.append(comb)
                return
            else:
                dfs(comb+")", open, close-1)
                dfs(comb+"(", open-1, close)

        dfs()
        return res

