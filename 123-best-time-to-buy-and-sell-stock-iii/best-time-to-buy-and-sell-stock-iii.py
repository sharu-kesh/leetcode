class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        diff1 = [0] * n
        diff2 = [0] * n
        mini = prices[0]
        profit = 0

        for i in range(1, n):
            mini = min(mini, prices[i])
            profit = max(profit, prices[i] - mini)
            diff1[i] = profit
        
        maxi = prices[-1]
        profit = 0

        for i in range(n - 2, -1, -1):
            maxi = max(maxi, prices[i])
            profit = max(profit, maxi - prices[i])
            diff2[i] = profit
        
        profit = 0
        for i in range(n - 1):
            profit = max(profit, diff1[i] + diff2[i])
        return max(profit, diff2[0], diff1[-1])