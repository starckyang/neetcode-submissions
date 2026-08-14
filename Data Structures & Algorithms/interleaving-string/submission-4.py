class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        l1, l2, l3=len(s1), len(s2), len(s3)
        if l3!=(l1+l2):
            return False

        dp={}
        def dfs(p1, p2, p3):
            if p3==len(s3):
                return True
            if (p1, p2, p3) in dp:
                return dp[(p1, p2, p3)]
            t=s3[p3]
            if p1<len(s1) and s1[p1]==t:
                if dfs(p1+1, p2, p3+1):
                    dp[(p1, p2, p3)]=True
                    return True
            if p2<len(s2) and s2[p2]==t:
                if dfs(p1, p2+1, p3+1):
                    dp[(p1, p2, p3)]=True
                    return True
            dp[(p1, p2, p3)]=False
            return False

        return dfs(0, 0, 0)
