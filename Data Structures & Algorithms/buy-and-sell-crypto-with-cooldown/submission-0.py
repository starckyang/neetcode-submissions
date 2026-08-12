class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp method, bottom up

        dp=[[0]*len(prices) for _ in range(len(prices)+1)] # range(k), k = trade+1
        # dp[i][j] = max(dp[i][j-1], pt-pc+dp[i-1][c-1])
        for k in range(1, len(prices)+1):
            low=prices[0]
            for i in range(1, len(prices)):
                if i==1:
                    low=min(low, prices[1])
                else:
                    low=min(low, prices[i]-dp[k-1][i-2])
                dp[k][i]=max(dp[k][i-1], prices[i]-low)
        
        return dp[-1][-1]