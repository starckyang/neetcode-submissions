class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cused=[-1]*(amount+1)
        cused[0]=0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0 and cused[i-coin]!=-1:
                    if cused[i]>(cused[i-coin]+1) or cused[i]==-1:
                        cused[i]=cused[i-coin]+1
        return cused[-1]
