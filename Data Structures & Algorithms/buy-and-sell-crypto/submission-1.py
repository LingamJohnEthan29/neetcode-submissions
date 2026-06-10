class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        i = 1
        N = len(prices)
        while i != N:
            profit = prices[i]-min(prices[:i])
            maxProfit = max(maxProfit, profit)
            i += 1
        return maxProfit