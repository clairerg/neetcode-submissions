class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_prices = prices[0]
        for p in prices:
            min_prices = min(min_prices, p)
            max_profit = max(max_profit, p - min_prices)
        return max_profit 
            
        
        