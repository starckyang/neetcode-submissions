class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={len(s):True}
        def dfs(pos):
            if pos in memo:
                return memo[pos]
            for word in wordDict:
                if s[pos:pos+len(word)]==word:
                    if dfs(pos+len(word))==True:
                        memo[pos]=1
                        return True
            memo[pos]=False
            return False

        return dfs(0)