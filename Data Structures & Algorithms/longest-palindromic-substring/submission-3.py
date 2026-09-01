class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen=1
        resIdx=-1
        dp=[[False]*len(s) for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i]==s[j] and ((j-2<i) or (dp[i+1][j-1]==True)):
                    dp[i][j]=True

                    if (j-i+1)>=resLen:
                        resLen=(j-i+1)
                        resIdx=i
        
        return s[resIdx:resIdx+resLen]