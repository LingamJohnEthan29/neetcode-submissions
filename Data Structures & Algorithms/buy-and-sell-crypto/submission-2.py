class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrices = prices[0]
        maxProfit = 0
        for price in prices:
            minPrices = min(price, minPrices)
            maxProfit = max(maxProfit, price-minPrices)
        return maxProfit