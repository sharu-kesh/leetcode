class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        pre = [0] * (2 * k + 1)
        cur = [0] * (2 * k + 1)

        for i in range(n - 1, - 1, -1):
            for j in range(2 * k):
                if j & 1:
                    cur[j] = max(pre[j + 1] + prices[i], pre[j])
                else:
                    cur[j] = max(pre[j + 1] - prices[i], pre[j])
            pre = cur
        return pre[0]