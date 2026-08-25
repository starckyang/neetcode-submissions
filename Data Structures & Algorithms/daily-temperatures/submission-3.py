class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #dp: storing the positions?
        dp=[len(temperatures)]*len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            j=i+1
            while j<len(temperatures) and temperatures[j]<=temperatures[i]:
                j=dp[j]
            dp[i]=j
        res=[]
        for i in range(len(dp)):
            if dp[i]==len(temperatures):
                res.append(0)
            else:
                res.append(dp[i]-i)
        return res