class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxPrice = 0
        price = prices[0]
        for i in range(1, len(prices)):
            price = min(price, prices[i])
            maxPrice = max(maxPrice, prices[i] - price)
            profit += maxPrice
            # print(maxPrice, profit, price)
            maxPrice = 0
            price = prices[i]
        return profit
        