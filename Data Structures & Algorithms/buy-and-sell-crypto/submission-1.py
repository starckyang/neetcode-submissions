class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ret = 0 
        start = prices[0]
        for price in prices:
            if price >= start:
                max_ret = max(price-start, max_ret) 
            else: 
                start = price
        return max_ret 