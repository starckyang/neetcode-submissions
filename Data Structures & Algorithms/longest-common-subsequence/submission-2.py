class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev=[0]*(len(text2)+1)
        cur=[0]*(len(text2)+1)
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    cur[j]=max(cur[j-1],
                               prev[j],
                               prev[j-1]+1)
                else:
                    cur[j]=max(cur[j-1],
                                 prev[j])
            prev=cur
            cur=[0]*(len(text2)+1)
        return prev[-1]
