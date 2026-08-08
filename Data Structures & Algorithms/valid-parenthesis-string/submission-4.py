class Solution:
    def checkValidString(self, s: str) -> bool:

        dp={(len(s), 0): True}
        
        def dfs(i, opens):
            if (i, opens) in dp:
                return dp[(i, opens)]
            if opens<0:
                return False
            if i == len(s):
                return opens==0
            if s[i]=="(":
                if dfs(i+1, opens+1):
                    dp[(i, opens)]=True
                    return True
                else:
                    dp[(i, opens)]=False
                    return False
            elif s[i] == ")":
                if dfs(i+1, opens-1):
                    dp[(i, opens)]=True
                    return True
                else:
                    dp[(i, opens)]=False
                    return False
            else:
                if (dfs(i+1, opens+1) or
                    dfs(i+1, opens) or 
                    dfs(i+1, opens-1)):
                    dp[(i, opens)]=True
                    return True
                else:
                    dp[(i, opens)]=False
                    return False
                
        
        return dfs(0, 0)