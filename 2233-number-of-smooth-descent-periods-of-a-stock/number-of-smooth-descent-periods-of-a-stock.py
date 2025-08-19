class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 1
        res = 0
        count = 1
        for i in range(1, n):
            if prices[i] - prices[i - 1] == -1:
                count += 1
            else:
                res += (count * (count + 1)) // 2
                count = 1
        if count:
            res += (count * (count + 1)) // 2
        return res
