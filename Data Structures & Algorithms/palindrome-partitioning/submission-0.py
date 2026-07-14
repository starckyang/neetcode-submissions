class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(start, end):
            while start <= end:
                if s[start] == s[end]:
                    start, end = start + 1, end - 1
                else:
                    return False
            return True

        res = []
        
        def dfs(cur_idx=0, comb=[]):
            if cur_idx >= len(s):
                res.append(comb.copy())
                return 
            end = len(s)-1
            while end >= cur_idx:
                if is_palindrome(cur_idx, end):
                    comb.append(s[cur_idx:end+1])
                    dfs(end+1, comb)
                    comb.pop()
                end -= 1


        dfs()
        return res