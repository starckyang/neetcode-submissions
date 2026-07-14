class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(comb="", idx=0):
            if idx >= len(digits):
                res.append(comb)
                return
            for char in phone_map[digits[idx]]:
                dfs(comb+char, idx+1)

        dfs()
        return res
            