class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        price = prices[0]
        for i in range(1, len(prices)):
            price = min(price, prices[i])
            maxPrice = max(maxPrice, prices[i] - price)
        return maxPrice
        