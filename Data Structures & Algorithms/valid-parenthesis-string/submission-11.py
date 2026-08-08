class Solution:
    def checkValidString(self, s: str) -> bool:
        # bottom up dfs
        rec=[False]*(len(s)+1)
        rec[0]=True
        for i in range(len(s)-1, -1, -1):
            if s[i]==")":
                rec=[False]+rec[:-1]
            elif s[i]=="(":
                rec[:-1]=rec[1:]+[False]
            else:
                new_rec=[False]*(len(s)+1)
                for j in range(len(s)):
                    if j==0:
                        new_rec[j] = (rec[j] or rec[j+1])
                    else:
                        new_rec[j] = (rec[j] or rec[j+1] or rec[j-1])
                rec=new_rec
        return rec[0]
